/**
 * DSA Progress Dashboard App
 * Vanilla ES2020+ JavaScript, zero dependencies.
 */

(function () {
  'use strict';

  // State elements
  const loadingEl = document.getElementById('loading-state');
  const errorEl = document.getElementById('error-state');
  const errorMsgEl = document.getElementById('error-message');
  const contentEl = document.getElementById('dashboard-content');
  const retryBtn = document.getElementById('retry-button');

  // Theme management
  function initTheme() {
    const saved = localStorage.getItem('dsa_theme');
    if (saved === 'dark' || saved === 'light') {
      document.documentElement.setAttribute('data-theme', saved);
    }
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    let next;
    if (!current) {
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      next = prefersDark ? 'light' : 'dark';
    } else {
      next = current === 'dark' ? 'light' : 'dark';
    }
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('dsa_theme', next);
    updateThemeButtonLabel();
  }

  function updateThemeButtonLabel() {
    const btn = document.getElementById('theme-toggle-btn');
    if (!btn) return;
    const current = document.documentElement.getAttribute('data-theme');
    const isDark = current ? current === 'dark' : window.matchMedia('(prefers-color-scheme: dark)').matches;
    btn.textContent = isDark ? '☀️ Light' : '🌙 Dark';
    btn.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
  }

  // Safe formatting helpers
  function escapeHtml(str) {
    if (str === null || str === undefined) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function pct(num, denom) {
    if (!denom || denom <= 0) return 0;
    return Math.round((num / denom) * 100);
  }

  // --------------------------------------------------------------------------
  // Panel Renderers (In exact specified display order: 1 to 8)
  // --------------------------------------------------------------------------

  // Panel 1: Header
  function renderHeader(data) {
    const state = data.state || {};
    const overall = data.overall || {};
    const lastUpdated = state.last_updated
      ? `Last session: ${escapeHtml(state.last_updated)}`
      : 'No sessions yet';
    const streak = overall.streak_days || 0;
    const generatedFor = data.generated_for || 'Unknown date';

    return `
      <header id="panel-header" class="card header-card">
        <div class="header-left">
          <h1>DSA Progress Dashboard</h1>
          <div class="header-subtitle">
            <span>📅 ${escapeHtml(lastUpdated)}</span>
            <span>·</span>
            <span>Report for: ${escapeHtml(generatedFor)}</span>
          </div>
        </div>
        <div class="header-right">
          <div class="streak-pill" role="status" aria-label="Current streak: ${streak} days">
            <span aria-hidden="true">🔥</span>
            <span>${streak} Day${streak === 1 ? '' : 's'} Streak</span>
          </div>
          <button id="theme-toggle-btn" class="btn" type="button" aria-label="Toggle theme">
            🌙 Dark
          </button>
        </div>
      </header>
    `;
  }

  // Panel 2: Today
  function renderToday(data) {
    const state = data.state || {};
    const dueList = data.reviews_due || [];
    const upcomingList = data.reviews_upcoming || [];
    const hasCurrentTopic = Boolean(state.current_topic);

    let reviewsDueHtml = '';
    if (dueList.length === 0) {
      reviewsDueHtml = '<div class="empty-state">No reviews due today 🎉</div>';
    } else {
      reviewsDueHtml = `
        <ul class="review-list">
          ${dueList.map(r => {
            const isOverdue = (r.days_overdue || 0) > 0;
            const badgeClass = isOverdue ? 'badge-overdue' : 'badge-due';
            const badgeText = isOverdue ? `Overdue ${r.days_overdue}d` : 'Due Today';
            return `
              <li class="review-item ${isOverdue ? 'overdue' : ''}">
                <div class="review-details">
                  <span class="review-topic">${escapeHtml(r.topic)}</span>
                  <span class="review-type">${escapeHtml(r.type || 'Review')} · Due ${escapeHtml(r.due)}</span>
                </div>
                <span class="badge ${badgeClass}">${escapeHtml(badgeText)}</span>
              </li>
            `;
          }).join('')}
        </ul>
      `;
    }

    let upcomingHtml = '';
    if (upcomingList.length > 0) {
      upcomingHtml = `
        <div style="margin-top: 1rem;">
          <h4 style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.4rem; text-transform: uppercase; letter-spacing: 0.05em;">
            Next 7 Days Agenda (${upcomingList.length})
          </h4>
          <ul class="review-list">
            ${upcomingList.map(r => `
              <li class="review-item">
                <div class="review-details">
                  <span class="review-topic" style="font-size: 0.9rem;">${escapeHtml(r.topic)}</span>
                  <span class="review-type">${escapeHtml(r.type || 'Review')} · In ${r.in_days} day${r.in_days === 1 ? '' : 's'} (${escapeHtml(r.due)})</span>
                </div>
                <span class="badge badge-todo">In ${r.in_days}d</span>
              </li>
            `).join('')}
          </ul>
        </div>
      `;
    }

    let resumptionHtml = '';
    if (hasCurrentTopic) {
      resumptionHtml = `
        <div class="resumption-card">
          <div class="resumption-header">Current Focus / Resume</div>
          <div class="resumption-title">${escapeHtml(state.current_topic)}</div>
          <div class="resumption-meta">
            Module ${escapeHtml(state.module_number || '-')}: ${escapeHtml(state.module_name || '')} · Status: <strong>${escapeHtml(state.topic_status || 'In Progress')}</strong>
          </div>
          <div class="resumption-cli">
            python scripts/dsa.py export
          </div>
        </div>
      `;
    } else {
      resumptionHtml = `
        <div class="resumption-card" style="background-color: var(--bg-subtle); border-color: var(--border-subtle);">
          <div class="resumption-header" style="color: var(--text-muted);">Current Focus</div>
          <p class="empty-state" style="padding: 0.5rem 0; text-align: left;">
            No active topic. Start a session with your Gemini mentor skill!
          </p>
        </div>
      `;
    }

    return `
      <section id="panel-today" class="card" aria-labelledby="today-heading">
        <div class="card-header">
          <h2 id="today-heading" class="card-title">
            <span aria-hidden="true">🎯</span> Today's Action Plan
          </h2>
          <span class="badge badge-due">${dueList.length} Due</span>
        </div>
        <div class="today-section">
          ${resumptionHtml}
          <div>
            <h3 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 0.5rem;">Spaced Reviews Due</h3>
            ${reviewsDueHtml}
            ${upcomingHtml}
          </div>
        </div>
      </section>
    `;
  }

  // Panel 3: Overall Progress
  function renderOverall(data) {
    const o = data.overall || {};
    const topicsDone = o.topics_done || 0;
    const topicsTotal = o.topics_total || 60;
    const topicsPct = pct(topicsDone, topicsTotal);

    const bankSolved = o.bank_solved || 0;
    const bankTotal = o.bank_total || 175;
    const bankPct = pct(bankSolved, bankTotal);

    const totalSolved = o.problems_solved_total || 0;
    const activeDays = o.active_days || 0;

    return `
      <section id="panel-overall" class="card" aria-labelledby="overall-heading">
        <div class="card-header">
          <h2 id="overall-heading" class="card-title">
            <span aria-hidden="true">📊</span> Overall Progress
          </h2>
          <span class="badge badge-bank">${topicsPct}% Syllabus</span>
        </div>
        
        <div class="stats-grid">
          <div class="stat-box">
            <div class="stat-label">Syllabus Topics</div>
            <div class="stat-value">${topicsDone} <span style="font-size: 0.9rem; font-weight: normal; color: var(--text-muted);">/ ${topicsTotal}</span></div>
            <div class="stat-sub">${topicsPct}% completed</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Core Practice Bank</div>
            <div class="stat-value">${bankSolved} <span style="font-size: 0.9rem; font-weight: normal; color: var(--text-muted);">/ ${bankTotal}</span></div>
            <div class="stat-sub">${bankPct}% solved</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Problems & Activity</div>
            <div class="stat-value">${totalSolved}</div>
            <div class="stat-sub">${activeDays} active day${activeDays === 1 ? '' : 's'}</div>
          </div>
        </div>

        <div class="progress-group">
          <div class="progress-header">
            <span>Syllabus Topics (${topicsDone}/${topicsTotal})</span>
            <span>${topicsPct}%</span>
          </div>
          <div class="progress-bar-container" role="progressbar" aria-valuenow="${topicsPct}" aria-valuemin="0" aria-valuemax="100" aria-label="Syllabus Topics Progress: ${topicsPct}%">
            <div class="progress-bar-fill ${topicsPct === 100 ? 'success' : ''}" style="width: ${topicsPct}%;"></div>
          </div>
        </div>

        <div class="progress-group" style="margin-bottom: 0;">
          <div class="progress-header">
            <span>Practice Bank Coverage (${bankSolved}/${bankTotal})</span>
            <span>${bankPct}%</span>
          </div>
          <div class="progress-bar-container" role="progressbar" aria-valuenow="${bankPct}" aria-valuemin="0" aria-valuemax="100" aria-label="Practice Bank Coverage: ${bankPct}%">
            <div class="progress-bar-fill ${bankPct === 100 ? 'success' : ''}" style="width: ${bankPct}%;"></div>
          </div>
        </div>
      </section>
    `;
  }

  // Panel 4: Modules
  function renderModules(data) {
    const modules = data.modules || [];

    const moduleCardsHtml = modules.map(m => {
      const done = m.topics_done || 0;
      const total = m.topics_total || 0;
      const inProg = m.topics_in_progress || 0;
      const modPct = pct(done, total);
      const isCompleted = done === total && total > 0;
      const hasProgress = inProg > 0 || (done > 0 && !isCompleted);

      const topics = m.topics || [];
      const topicsHtml = topics.map(t => {
        let badgeClass = 'badge-todo';
        let icon = '○';
        let text = 'Todo';

        if (t.status === 'completed') {
          badgeClass = 'badge-completed';
          icon = '✓';
          text = 'Completed';
        } else if (t.status === 'in_progress') {
          badgeClass = 'badge-in-progress';
          icon = '⏳';
          text = 'In Progress';
        }

        return `
          <li class="topic-row">
            <span>${escapeHtml(t.name)}</span>
            <span class="badge ${badgeClass}"><span aria-hidden="true">${icon}</span> ${text}</span>
          </li>
        `;
      }).join('');

      return `
        <details class="module-details" data-status="${isCompleted ? 'completed' : hasProgress ? 'in_progress' : 'todo'}">
          <summary class="module-summary">
            <div class="module-summary-row">
              <span class="module-name">Module ${m.number}: ${escapeHtml(m.name)}</span>
              <span class="module-progress-text">
                ${done}/${total} ${inProg > 0 ? `(+${inProg} active)` : ''}
              </span>
            </div>
            <div class="progress-bar-container" role="progressbar" aria-valuenow="${modPct}" aria-valuemin="0" aria-valuemax="100" aria-label="Module ${m.number} ${escapeHtml(m.name)} Progress: ${modPct}%">
              <div class="progress-bar-fill ${isCompleted ? 'success' : ''}" style="width: ${modPct}%;"></div>
            </div>
          </summary>
          <div class="topics-table-container">
            <ul class="topics-list">
              ${topicsHtml}
            </ul>
          </div>
        </details>
      `;
    }).join('');

    return `
      <section id="panel-modules" class="card" aria-labelledby="modules-heading">
        <div class="card-header">
          <h2 id="modules-heading" class="card-title">
            <span aria-hidden="true">📚</span> Curriculum Modules (${modules.length})
          </h2>
          <div class="module-filters" role="group" aria-label="Filter modules by status">
            <button class="filter-btn active" data-filter="all">All (${modules.length})</button>
            <button class="filter-btn" data-filter="in_progress">Active</button>
            <button class="filter-btn" data-filter="completed">Completed</button>
          </div>
        </div>
        <div class="module-list">
          ${moduleCardsHtml}
        </div>
      </section>
    `;
  }

  // Panel 5: Activity Heatmap
  function renderActivity(data) {
    const activity = data.activity || {};
    const generatedFor = data.generated_for || new Date().toISOString().slice(0, 10);
    const [y, m, d] = generatedFor.split('-').map(Number);
    const endDate = new Date(Date.UTC(y, m - 1, d));

    // Align to Saturday of current week to construct 7-row columns
    const endDayOfWeek = endDate.getUTCDay();
    const gridEnd = new Date(endDate);
    gridEnd.setUTCDate(gridEnd.getUTCDate() + (6 - endDayOfWeek));

    // 26 weeks back = 182 days
    const totalDays = 26 * 7;
    const gridStart = new Date(gridEnd);
    gridStart.setUTCDate(gridStart.getUTCDate() - totalDays + 1);

    const cellsHtml = [];
    const cur = new Date(gridStart);

    while (cur <= gridEnd) {
      const isoStr = cur.toISOString().slice(0, 10);
      const count = activity[isoStr] || 0;
      let level = 0;
      if (count === 1) level = 1;
      else if (count === 2) level = 2;
      else if (count === 3) level = 3;
      else if (count >= 4) level = 4;

      const dateLabel = `${isoStr}: ${count} event${count === 1 ? '' : 's'}`;
      cellsHtml.push(`
        <div class="heatmap-cell"
             data-level="${level}"
             title="${escapeHtml(dateLabel)}"
             tabindex="0"
             role="gridcell"
             aria-label="${escapeHtml(dateLabel)}"></div>
      `);
      cur.setUTCDate(cur.getUTCDate() + 1);
    }

    const activeDaysCount = data.overall?.active_days || Object.keys(activity).length;

    return `
      <section id="panel-activity" class="card" aria-labelledby="activity-heading">
        <div class="card-header">
          <h2 id="activity-heading" class="card-title">
            <span aria-hidden="true">📈</span> 26-Week Study Heatmap
          </h2>
          <span class="badge badge-due">${activeDaysCount} Active Days</span>
        </div>
        <p class="sr-only">Activity calendar for past 26 weeks. Total active days: ${activeDaysCount}.</p>
        <div class="heatmap-container" role="grid" aria-label="Study activity heatmap">
          <div class="heatmap-grid">
            ${cellsHtml.join('')}
          </div>
        </div>
        <div class="heatmap-legend" aria-hidden="true">
          <span>Less</span>
          <div class="heatmap-cell heatmap-legend-cell" data-level="0"></div>
          <div class="heatmap-cell heatmap-legend-cell" data-level="1"></div>
          <div class="heatmap-cell heatmap-legend-cell" data-level="2"></div>
          <div class="heatmap-cell heatmap-legend-cell" data-level="3"></div>
          <div class="heatmap-cell heatmap-legend-cell" data-level="4"></div>
          <span>More</span>
        </div>
      </section>
    `;
  }

  // Panel 6: Practice
  function renderPractice(data) {
    const recent = data.recent_solved || [];

    let tableContent = '';
    if (recent.length === 0) {
      tableContent = `
        <div class="empty-state">
          No problems solved yet. Run <code>python scripts/dsa.py new &lt;lc&gt;</code> to start your first problem!
        </div>
      `;
    } else {
      tableContent = `
        <div class="table-responsive">
          <table class="data-table" aria-label="Recently solved LeetCode problems">
            <thead>
              <tr>
                <th scope="col">Problem</th>
                <th scope="col">Difficulty</th>
                <th scope="col">Topic / Group</th>
                <th scope="col">Attempts</th>
                <th scope="col">Hints</th>
                <th scope="col">Solved</th>
              </tr>
            </thead>
            <tbody>
              ${recent.map(r => {
                const num = r.id ? r.id.replace(/^LC/i, '') : '?';
                const diff = r.difficulty || '?';
                let diffBadgeClass = 'badge-todo';
                if (/easy/i.test(diff)) diffBadgeClass = 'badge-easy';
                else if (/medium|med/i.test(diff)) diffBadgeClass = 'badge-medium';
                else if (/hard/i.test(diff)) diffBadgeClass = 'badge-hard';

                return `
                  <tr>
                    <td>
                      <span class="problem-id">LC ${escapeHtml(num)}</span>: 
                      <span style="font-weight: 600;">${escapeHtml(r.title)}</span>
                      ${r.in_bank ? '<span class="badge badge-bank" style="margin-left: 0.3rem;">Bank</span>' : ''}
                    </td>
                    <td><span class="badge ${diffBadgeClass}">${escapeHtml(diff)}</span></td>
                    <td>${escapeHtml(r.group || (r.module ? `Module ${r.module}` : '-'))}</td>
                    <td>${r.attempts ?? 0}</td>
                    <td>${r.hints ?? 0}</td>
                    <td><span class="mistake-date">${escapeHtml(r.first_solved || '-')}</span></td>
                  </tr>
                `;
              }).join('')}
            </tbody>
          </table>
        </div>
      `;
    }

    return `
      <section id="panel-practice" class="card" aria-labelledby="practice-heading">
        <div class="card-header">
          <h2 id="practice-heading" class="card-title">
            <span aria-hidden="true">💻</span> Practice & Recent Solved (${recent.length})
          </h2>
          <span class="badge badge-bank">Bank Solved: ${data.overall?.bank_solved || 0}</span>
        </div>
        ${tableContent}
      </section>
    `;
  }

  // Panel 7: Focus & Memory
  function renderFocus(data) {
    const weak = data.weak_areas || [];
    const homework = data.homework || [];
    const mistakes = data.mistakes_recent || [];

    const weakHtml = weak.length === 0
      ? '<p class="empty-state" style="padding: 0.2rem 0; text-align: left;">No weak areas recorded.</p>'
      : `<div class="tag-list">${weak.map(w => `<span class="tag-item weak"><span aria-hidden="true">⚠️</span> ${escapeHtml(w)}</span>`).join('')}</div>`;

    const hwHtml = homework.length === 0
      ? '<p class="empty-state" style="padding: 0.2rem 0; text-align: left;">No homework currently assigned.</p>'
      : `<ul style="list-style: disc; padding-left: 1.25rem; font-size: 0.9rem; display: flex; flex-direction: column; gap: 0.35rem;">
          ${homework.map(h => `<li>${escapeHtml(h)}</li>`).join('')}
         </ul>`;

    const mistakesHtml = mistakes.length === 0
      ? '<p class="empty-state" style="padding: 0.2rem 0; text-align: left;">No mistakes logged yet.</p>'
      : `
        <details class="mistakes-accordion">
          <summary class="mistakes-summary">
            View Mistakes Log (${mistakes.length})
          </summary>
          <div class="mistakes-content">
            <ul class="mistakes-list">
              ${mistakes.map(m => `
                <li>
                  <span class="mistake-date">[${escapeHtml(m.date)}]</span>
                  <span>${escapeHtml(m.text)}</span>
                </li>
              `).join('')}
            </ul>
          </div>
        </details>
      `;

    return `
      <section id="panel-focus" class="card" aria-labelledby="focus-heading">
        <div class="card-header">
          <h2 id="focus-heading" class="card-title">
            <span aria-hidden="true">🧠</span> Focus & Memory Retention
          </h2>
        </div>
        <div class="focus-grid">
          <div>
            <h3 style="font-size: 0.9rem; font-weight: 700; margin-bottom: 0.4rem; color: var(--warning);">
              Weak Areas to Reinforce
            </h3>
            ${weakHtml}
          </div>
          <div>
            <h3 style="font-size: 0.9rem; font-weight: 700; margin-bottom: 0.4rem; color: var(--accent);">
              Homework Assignments
            </h3>
            ${hwHtml}
          </div>
          <div>
            <h3 style="font-size: 0.9rem; font-weight: 700; margin-bottom: 0.4rem;">
              Mistakes Log
            </h3>
            ${mistakesHtml}
          </div>
        </div>
      </section>
    `;
  }

  // Panel 8: Patterns
  function renderPatterns(data) {
    const patterns = data.patterns || {};
    const entries = Object.entries(patterns);

    let content = '';
    if (entries.length === 0) {
      content = '<div class="empty-state">No pattern evaluations logged yet.</div>';
    } else {
      content = `
        <div class="pattern-grid">
          ${entries.map(([name, info]) => {
            const conf = (info && info.confidence) ? String(info.confidence) : 'Unrated';
            let confClass = 'badge-conf-none';
            if (/high/i.test(conf)) confClass = 'badge-conf-high';
            else if (/med/i.test(conf)) confClass = 'badge-conf-med';
            else if (/low/i.test(conf)) confClass = 'badge-conf-low';

            const solved = info && info.questions_solved ? info.questions_solved : 0;

            return `
              <div class="pattern-card">
                <div>
                  <div class="pattern-name">${escapeHtml(name)}</div>
                  <div class="pattern-count">${solved} solved</div>
                </div>
                <span class="badge ${confClass}">${escapeHtml(conf)}</span>
              </div>
            `;
          }).join('')}
        </div>
      `;
    }

    return `
      <section id="panel-patterns" class="card" aria-labelledby="patterns-heading">
        <div class="card-header">
          <h2 id="patterns-heading" class="card-title">
            <span aria-hidden="true">🧩</span> Pattern Mastery (${entries.length})
          </h2>
        </div>
        ${content}
      </section>
    `;
  }

  // --------------------------------------------------------------------------
  // Main Assembly & Event Binding
  // --------------------------------------------------------------------------

  function renderDashboard(data) {
    // Exactly 8 panels rendered in the specified sequential display order:
    // 1. Header -> 2. Today -> 3. Overall -> 4. Modules -> 5. Activity -> 6. Practice -> 7. Focus -> 8. Patterns
    contentEl.innerHTML = `
      <div class="dashboard-grid">
        ${renderHeader(data)}
        ${renderToday(data)}
        ${renderOverall(data)}
        ${renderModules(data)}
        ${renderActivity(data)}
        ${renderPractice(data)}
        ${renderFocus(data)}
        ${renderPatterns(data)}
      </div>
    `;

    // Event listener: Theme toggle
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) {
      themeBtn.addEventListener('click', toggleTheme);
      updateThemeButtonLabel();
    }

    // Event listener: Module Filters
    const filterBtns = contentEl.querySelectorAll('.filter-btn');
    const moduleCards = contentEl.querySelectorAll('.module-details');

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.getAttribute('data-filter');
        moduleCards.forEach(card => {
          const cardStatus = card.getAttribute('data-status');
          if (filter === 'all') {
            card.style.display = '';
          } else if (filter === 'completed') {
            card.style.display = cardStatus === 'completed' ? '' : 'none';
          } else if (filter === 'in_progress') {
            card.style.display = cardStatus === 'in_progress' ? '' : 'none';
          }
        });
      });
    });
  }

  // --------------------------------------------------------------------------
  // Data Fetching & Error Handling
  // --------------------------------------------------------------------------

  function loadProgress() {
    loadingEl.style.display = 'block';
    errorEl.style.display = 'none';
    contentEl.style.display = 'none';

    fetch('progress.json', { cache: 'no-cache' })
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP Error ${response.status} (${response.statusText})`);
        }
        return response.json();
      })
      .then(data => {
        loadingEl.style.display = 'none';
        renderDashboard(data);
        contentEl.style.display = 'block';
      })
      .catch(err => {
        loadingEl.style.display = 'none';
        errorMsgEl.textContent = `Error: ${err.message}`;
        errorEl.style.display = 'block';
      });
  }

  // Retry button handler
  if (retryBtn) {
    retryBtn.addEventListener('click', loadProgress);
  }

  // Initialize
  initTheme();
  loadProgress();

})();
