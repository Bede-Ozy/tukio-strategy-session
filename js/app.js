// ==========================================================================
// TUKIO KONSULTS LTD - 2026 STRATEGY SESSION
// Presentation Controller Engine
// Strictly aligned with "Tukio Konsult Strategy Session Agenda.pdf"
// ==========================================================================

document.addEventListener("DOMContentLoaded", () => {
  const slides = (typeof tukioStrategyData !== "undefined") ? tukioStrategyData : [];
  let currentIndex = 0;
  let autoplayInterval = null;
  let isAutoplayActive = false;
  let currentTheme = "dark";
  let activeFilterSession = "all";

  // DOM Elements Cache
  const container = document.getElementById("presentation-container");
  const wrapper = document.getElementById("slide-wrapper");
  const slideBody = document.getElementById("slide-body");
  const slideHeader = document.getElementById("slide-header-el");
  const slideFooter = document.getElementById("slide-footer-el");
  const slideCategory = document.getElementById("slide-category");
  const slideTitle = document.getElementById("slide-title");
  const slideSubtitle = document.getElementById("slide-subtitle");
  const slideNumber = document.getElementById("slide-number");
  const footerSessionText = document.getElementById("footer-session-text");
  const slideIndicator = document.getElementById("slide-indicator");
  const progressFill = document.getElementById("progress-fill");
  const playIcon = document.getElementById("play-icon");

  // Navigation Buttons
  const btnPrev = document.getElementById("btn-prev");
  const btnNext = document.getElementById("btn-next");
  const btnPlay = document.getElementById("btn-play");
  const btnNotes = document.getElementById("btn-notes");
  const btnTheme = document.getElementById("btn-theme");
  const btnFullscreen = document.getElementById("btn-fullscreen");

  // Sidebar Elements
  const sidebar = document.getElementById("agenda-sidebar");
  const sidebarOverlay = document.getElementById("sidebar-overlay");
  const btnToggleSidebar = document.getElementById("btn-toggle-sidebar");
  const btnCloseSidebar = document.getElementById("btn-close-sidebar");
  const sidebarSlidesList = document.getElementById("sidebar-slides-list");

  // Speaker Notes Elements
  const notesDrawer = document.getElementById("speaker-notes-drawer");
  const notesContent = document.getElementById("speaker-notes-content");
  const btnCloseNotes = document.getElementById("btn-close-notes");

  // Timer Modal Elements
  const timerModal = document.getElementById("timer-modal");
  const btnTimerModal = document.getElementById("btn-timer-modal");
  const btnCloseTimerModal = document.getElementById("btn-close-timer-modal");
  const modalTimerDigits = document.getElementById("modal-timer-digits");
  const modalBtnStart = document.getElementById("modal-btn-start");
  const modalBtnReset = document.getElementById("modal-btn-reset");
  const headerTimerBadge = document.getElementById("header-timer-badge");
  const headerTimerDisplay = document.getElementById("header-timer-display");

  // Timer State
  let timerDuration = 300; // 5 mins default
  let timerRemaining = 300;
  let timerInterval = null;
  let isTimerRunning = false;

  // START | STOP | CONTINUE Interactive Card State
  let sscActiveIndex = 0; // 0: START, 1: STOP, 2: CONTINUE, 3: ALL VIEW
  let sscCardTimes = [300, 300, 300]; // 5 minutes each default
  let sscRunningIndex = -1; // -1 if not running
  let sscInterval = null;

  function stopSscTimer() {
    if (sscInterval) {
      clearInterval(sscInterval);
      sscInterval = null;
    }
    sscRunningIndex = -1;
  }

  // SWOT Interactive Card State
  let swotActiveIndex = 0; // 0: STRENGTHS, 1: WEAKNESSES, 2: OPPORTUNITIES, 3: THREATS, 4: ALL VIEW
  let swotCardTimes = [300, 300, 300, 300]; // 5 minutes each default
  let swotRunningIndex = -1; // -1 if not running
  let swotInterval = null;

  function stopSwotTimer() {
    if (swotInterval) {
      clearInterval(swotInterval);
      swotInterval = null;
    }
    swotRunningIndex = -1;
  }

  // 1. SCALING ENGINE: Math calculation to scale 1920x1080 stage to viewport
  function scaleSlide() {
    if (!wrapper || !container) return;
    const targetW = 1920;
    const targetH = 1080;
    const containerW = container.clientWidth;
    const containerH = container.clientHeight;

    const scaleX = containerW / targetW;
    const scaleY = containerH / targetH;
    const scale = Math.min(scaleX, scaleY) * 0.96; // 96% fit for elegant border margin

    wrapper.style.transform = `translate(-50%, -50%) scale(${scale})`;
  }

  window.addEventListener("resize", scaleSlide);
  scaleSlide();

  // 2. SLIDE RENDERER
  function renderSlide(index) {
    if (!slides || slides.length === 0) return;
    if (index < 0) index = 0;
    if (index >= slides.length) index = slides.length - 1;
    currentIndex = index;

    // Stop any active interactive timers when changing slides
    stopSscTimer();
    stopSwotTimer();

    const slide = slides[currentIndex];

    // Slide Header updates
    if (slide.layout === "title-cover") {
      slideHeader.style.display = "none";
      slideFooter.style.display = "none";
    } else {
      slideHeader.style.display = "flex";
      slideFooter.style.display = "flex";
      slideCategory.textContent = slide.category || "STRATEGY SESSION";
      slideTitle.textContent = slide.title || "";
      if (slide.subtitle) {
        slideSubtitle.textContent = slide.subtitle;
        slideSubtitle.style.display = "block";
      } else {
        slideSubtitle.style.display = "none";
      }
    }

    // Slide Footer updates
    footerSessionText.textContent = slide.session ? `${slide.session} • Tukio 2026 Strategy` : "2026 Strategy Session";
    slideNumber.textContent = `Slide ${currentIndex + 1} of ${slides.length}`;
    slideIndicator.textContent = `${currentIndex + 1} / ${slides.length}`;
    progressFill.style.width = `${((currentIndex + 1) / slides.length) * 100}%`;

    // Takeaway Footer updates: Extra footer content strictly at bottom of slide canvas
    const takeawayEl = document.getElementById("slide-takeaway-el");
    const takeawayTextEl = document.getElementById("slide-takeaway-text");
    if (takeawayEl && takeawayTextEl) {
      if (slide.takeaway && slide.layout !== "title-cover") {
        takeawayTextEl.textContent = slide.takeaway;
        takeawayEl.style.display = "flex";
      } else {
        takeawayEl.style.display = "none";
      }
    }

    // Render Body according to Layout
    renderLayout(slide, slideBody);

    // Update Speaker Notes Drawer Content
    updateSpeakerNotes(slide);

    // Update Top Session Nav active state
    updateSessionNav(slide.session);

    // Update Sidebar Active Item
    updateSidebarActiveState();

    // Trigger scaling
    scaleSlide();
  }

  // 3. LAYOUT DISPATCHER (ONLY TALKING POINTS, TOPICS, AND CARDS)
  function renderLayout(slide, containerEl) {
    containerEl.innerHTML = "";

    switch (slide.layout) {
      case "title-cover":
        renderTitleCover(slide, containerEl);
        break;
      case "agenda-table":
        renderAgendaTable(slide, containerEl);
        break;
      case "talking-points-grid":
        renderTalkingPointsGrid(slide, containerEl);
        break;
      case "energiser-activity":
        renderEnergiserActivity(slide, containerEl);
        break;
      case "journey-points-8":
        renderJourneyPoints8(slide, containerEl);
        break;
      case "start-stop-continue-interactive":
      case "start-stop-continue-headers":
        renderTimedDiscussionFlow(slide, containerEl, "ssc");
        break;
      case "swot-board-interactive":
      case "swot-board-headers":
        renderTimedDiscussionFlow(slide, containerEl, "swot");
        break;
      case "break-card":
        renderBreakCard(slide, containerEl);
        break;
      case "matrix-framework":
        renderMatrixFramework(slide, containerEl);
        break;
      default:
        renderGenericSlide(slide, containerEl);
        break;
    }
  }

  // --------------------------------------------------------------------------
  // LAYOUT BUILDERS (ONLY TALKING POINTS, TOPICS, AND CARDS)
  // --------------------------------------------------------------------------

  // Slide 1: Title Cover
  function renderTitleCover(slide, containerEl) {
    containerEl.innerHTML = `
      <div class="layout-title-container">
        <div class="title-card">
          <div style="display: flex; justify-content: center; align-items: center; gap: 20px; margin-bottom: 25px;">
            <img src="images/tukio_logo.jpg" alt="Tukio Konsults" class="tukio-cover-logo">
            <div style="width: 1px; height: 45px; background: rgba(255,255,255,0.2);"></div>
            <img src="images/shamzbridge-logo.png" alt="Shamzbridge Consult" style="height: 60px; object-fit: contain;">
          </div>
          <h2>${slide.title}</h2>
          <h3>${slide.subtitle}</h3>
          <div class="title-meta-grid">
            <div class="meta-item">
              <span class="meta-label">FACILITATOR</span>
              <span class="meta-val">${slide.facilitator}</span>
            </div>
            <div class="meta-item">
              <span class="meta-label">HOST</span>
              <span class="meta-val">${slide.host}</span>
            </div>
            <div class="meta-item">
              <span class="meta-label">DATE & VENUE</span>
              <span class="meta-val">${slide.date}<br><small style="font-size: 0.95rem; color: var(--text-muted); font-weight: 500;">${slide.venue}</small></span>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  // Slide 2: Master Agenda Table
  function renderAgendaTable(slide, containerEl) {
    const rowsHtml = (slide.schedule || []).map((row, i) => `
      <tr class="${row.session.includes('Break') || row.session.includes('Lunch') ? 'agenda-break-row' : ''}">
        <td style="font-family: 'Outfit'; font-weight: 800; color: var(--brand-orange); white-space: nowrap; font-size: 1.15rem;">
          ${row.time}
        </td>
        <td style="font-weight: 600; font-size: 1.25rem; color: var(--slide-color);">
          ${row.session}
        </td>
        <td style="color: var(--text-muted); font-size: 1.15rem; font-weight: 500;">
          ${row.lead}
        </td>
      </tr>
    `).join("");

    containerEl.innerHTML = `
      <div class="agenda-table-wrapper">
        <table class="agenda-schedule-table">
          <thead>
            <tr>
              <th style="width: 220px;">Time</th>
              <th>Session</th>
              <th style="width: 320px;">Lead / Method</th>
            </tr>
          </thead>
          <tbody>
            ${rowsHtml}
          </tbody>
        </table>
      </div>
    `;
  }

  // Talking Points 3-Card Grid
  function renderTalkingPointsGrid(slide, containerEl) {
    const cardsHtml = (slide.cards || []).map(card => {
      const questionHtml = card.question ? `
        <div class="card-discussion-question">
          <i class="ri-question-line"></i>
          <span>${card.question}</span>
        </div>
      ` : "";

      const ptsHtml = (card.points || []).map(pt => `
        <div class="point-row">
          <span class="point-bullet">•</span>
          <span class="point-text">${pt}</span>
        </div>
      `).join("");

      return `
        <div class="talking-point-card">
          <div class="card-top-icon">
            <i class="${card.icon}"></i>
          </div>
          <h4 class="card-topic-title">${card.title}</h4>
          ${questionHtml}
          <div class="card-points-list">
            ${ptsHtml}
          </div>
        </div>
      `;
    }).join("");

    containerEl.innerHTML = `
      <div class="talking-points-row">
        ${cardsHtml}
      </div>
    `;
  }

  // Energiser & The Tukio Connection (Pair Activity with Timer)
  function renderEnergiserActivity(slide, containerEl) {
    const promptsHtml = (slide.prompts || []).map(p => `
      <div class="energiser-prompt-card">
        <span class="prompt-tag-badge">${p.tag}</span>
        <h4 class="prompt-main-question">${p.q}</h4>
        <span class="prompt-sub-caption">${p.sub}</span>
      </div>
    `).join("");

    containerEl.innerHTML = `
      <div class="energiser-container">
        <div class="energiser-prompts-col">
          ${promptsHtml}
        </div>
        <div class="energiser-timer-col">
          <div class="timer-box">
            <div class="timer-label"><i class="ri-time-line"></i> 5-Minute Pair Activity</div>
            <div class="timer-digits" id="slide-timer-digits">05:00</div>
            <div class="timer-controls">
              <button class="timer-action-btn" id="slide-btn-timer-toggle">
                <i class="ri-play-fill" id="slide-timer-icon"></i> <span id="slide-timer-btn-text">Start Timer</span>
              </button>
              <button class="timer-reset-btn" id="slide-btn-timer-reset">Reset</button>
            </div>
            <p style="font-size: 1.1rem; color: var(--text-muted); margin-top: 10px;">
              Pairs discuss for 5 minutes ➔ Introduce partner ➔ Capture on flipchart
            </p>
          </div>
        </div>
      </div>
    `;

    // Hook timer on this slide
    const slideTimerToggle = document.getElementById("slide-btn-timer-toggle");
    const slideTimerReset = document.getElementById("slide-btn-timer-reset");
    const slideTimerDigits = document.getElementById("slide-timer-digits");
    const slideTimerIcon = document.getElementById("slide-timer-icon");
    const slideTimerBtnText = document.getElementById("slide-timer-btn-text");

    if (slideTimerToggle) {
      slideTimerToggle.addEventListener("click", () => {
        toggleTimer();
        updateSlideTimerUI();
      });
    }
    if (slideTimerReset) {
      slideTimerReset.addEventListener("click", () => {
        resetTimer(300);
        updateSlideTimerUI();
      });
    }

    function updateSlideTimerUI() {
      if (slideTimerDigits) slideTimerDigits.textContent = formatTime(timerRemaining);
      if (slideTimerIcon && slideTimerBtnText) {
        if (isTimerRunning) {
          slideTimerIcon.className = "ri-pause-fill";
          slideTimerBtnText.textContent = "Pause";
        } else {
          slideTimerIcon.className = "ri-play-fill";
          slideTimerBtnText.textContent = "Start";
        }
      }
    }
  }

  // Moments in the Journey (8 Cards: a to h)
  function renderJourneyPoints8(slide, containerEl) {
    const cardsHtml = (slide.dimensions || []).map(d => `
      <div class="journey-dimension-card">
        <span class="dimension-letter">${d.letter}.</span>
        <h4 class="dimension-label">${d.label}</h4>
        <span class="dimension-hint">Discussion Point</span>
      </div>
    `).join("");

    containerEl.innerHTML = `
      <div class="journey-eight-container">
        ${cardsHtml}
      </div>
    `;
  }

  // ==========================================================================
  // TIMED DISCUSSION CARDS ENGINE (START | STOP | CONTINUE & SWOT ANALYSIS)
  // ==========================================================================
  function renderTimedDiscussionFlow(slide, containerEl, flowType) {
    const isSwot = (flowType === "swot");
    const cols = slide.columns || [];
    const totalCols = cols.length;

    function getActiveIndex() {
      return isSwot ? swotActiveIndex : sscActiveIndex;
    }
    function setActiveIndex(val) {
      if (isSwot) swotActiveIndex = val;
      else sscActiveIndex = val;
    }
    function getTimes() {
      return isSwot ? swotCardTimes : sscCardTimes;
    }
    function getRunningIndex() {
      return isSwot ? swotRunningIndex : sscRunningIndex;
    }
    function setRunningIndex(val) {
      if (isSwot) swotRunningIndex = val;
      else sscRunningIndex = val;
    }
    function stopTimer() {
      if (isSwot) stopSwotTimer();
      else stopSscTimer();
    }
    function setIntervalHandle(handle) {
      if (isSwot) swotInterval = handle;
      else sscInterval = handle;
    }

    const containerClass = isSwot ? "swot-interactive-container" : "ssc-interactive-container";
    const gridClass = isSwot ? "swot-interactive-cards-row" : "ssc-cards-row";
    const cardBaseClass = isSwot ? "swot-interactive-card" : "ssc-interactive-card";
    const cardPrefix = isSwot ? "swot" : "ssc";

    function updateView() {
      const activeIndex = getActiveIndex();
      const times = getTimes();
      const runningIndex = getRunningIndex();

      const cardsHtml = cols.map((col, idx) => {
        const isCurrent = (activeIndex === idx);
        const isCompleted = (activeIndex > idx && activeIndex !== totalCols);
        const isAllView = (activeIndex === totalCols);

        let stateSuffix = "dimmed";
        let statusBadge = `<span class="ssc-status-badge upcoming"><i class="ri-time-line"></i> UPCOMING</span>`;
        if (isCurrent) {
          stateSuffix = "active";
          statusBadge = `<span class="ssc-status-badge active"><i class="ri-record-circle-fill"></i> IN DISCUSSION</span>`;
        } else if (isAllView) {
          stateSuffix = "all-active";
          statusBadge = `<span class="ssc-status-badge completed"><i class="ri-check-double-line"></i> REVIEW</span>`;
        } else if (isCompleted) {
          stateSuffix = "completed";
          statusBadge = `<span class="ssc-status-badge completed"><i class="ri-check-line"></i> COMPLETED</span>`;
        }

        const isTimerActive = (runningIndex === idx);
        const cardTime = times[idx] !== undefined ? times[idx] : 300;

        // Round Timer Controls under the dial: Only on current active card or All View
        const underControlsHtml = (isCurrent || isAllView) ? `
          <div class="round-timer-under">
            <button class="round-adjust-btn" data-card="${idx}" data-adjust="-60" title="Minus 1 Minute">-1</button>
            <button class="round-play-btn ${isTimerActive ? 'running' : ''}" data-card="${idx}" title="${isTimerActive ? 'Pause' : 'Start Timer'}">
              <i class="${isTimerActive ? 'ri-pause-fill' : 'ri-play-fill'}"></i>
            </button>
            <button class="round-adjust-btn" data-card="${idx}" data-adjust="60" title="Plus 1 Minute">+1</button>
            <button class="round-reset-btn" data-card="${idx}" title="Reset Timer to 5:00">
              <i class="ri-restart-line"></i>
            </button>
          </div>
        ` : ``;

        // Round Timer Dial (centered time inside circle, no extra text)
        const timerDialHtml = `
          <div class="round-timer-wrapper">
            <div class="round-timer-dial dial-${col.type} ${isTimerActive ? 'running' : ''} ${cardTime === 0 ? 'time-elapsed' : ''}">
              <span class="round-timer-digits" id="${flowType}-clock-${idx}">${formatTime(cardTime)}</span>
            </div>
            ${underControlsHtml}
          </div>
        `;

        // Bottom Action Button
        let actionBtnHtml = "";
        if (isCurrent) {
          const isLast = (idx === cols.length - 1);
          actionBtnHtml = `
            <button class="ssc-next-plan-btn" data-next-step="${idx + 1}">
              <span>${col.nextLabel}</span>
              <i class="${isLast ? 'ri-checkbox-circle-line' : 'ri-arrow-right-line'}"></i>
            </button>
          `;
        } else if (isAllView) {
          actionBtnHtml = `
            <button class="ssc-jump-focus-btn" data-step="${idx}">
              <i class="ri-focus-3-line"></i> Focus
            </button>
          `;
        } else if (isCompleted) {
          actionBtnHtml = `
            <button class="ssc-reopen-btn" data-step="${idx}">
              <i class="ri-restart-line"></i> Re-open
            </button>
          `;
        }

        const cardClass = `${cardBaseClass} ${cardPrefix}-${col.type} ${cardPrefix}-card-${stateSuffix}`;

        return `
          <div class="${cardClass}" data-index="${idx}">
            <div class="ssc-card-top-header">
              <div class="ssc-top-meta">
                <span class="ssc-phase-pill">${col.phase || `Step ${idx + 1}`}</span>
                ${statusBadge}
              </div>
              <h3 class="ssc-card-title">${col.title}</h3>
            </div>

            <div class="ssc-card-body-content">
              <div class="ssc-prompt-card-section">
                <span class="ssc-prompt-header-tag"><i class="ri-chat-voice-line"></i> DISCUSSION TOPIC</span>
                <p class="ssc-prompt-question">${col.prompt}</p>
              </div>

              ${timerDialHtml}
            </div>

            <div class="ssc-card-bottom-actions">
              ${actionBtnHtml}
            </div>
          </div>
        `;
      }).join("");

      containerEl.innerHTML = `
        <div class="${containerClass}">
          <div class="${gridClass}">
            ${cardsHtml}
          </div>
        </div>
      `;

      attachEvents();
    }

    function attachEvents() {
      // Re-open and focus buttons
      containerEl.querySelectorAll(".ssc-reopen-btn, .ssc-jump-focus-btn").forEach(btn => {
        btn.addEventListener("click", (e) => {
          e.stopPropagation();
          stopTimer();
          setActiveIndex(parseInt(btn.getAttribute("data-step")));
          updateView();
        });
      });

      // Next Plan button
      containerEl.querySelectorAll(".ssc-next-plan-btn").forEach(btn => {
        btn.addEventListener("click", (e) => {
          e.stopPropagation();
          stopTimer();
          const nextStep = parseInt(btn.getAttribute("data-next-step"));
          setActiveIndex(nextStep);
          updateView();
        });
      });

      // Timer Play/Pause toggle
      containerEl.querySelectorAll(".round-play-btn").forEach(btn => {
        btn.addEventListener("click", (e) => {
          e.stopPropagation();
          const cardIdx = parseInt(btn.getAttribute("data-card"));
          toggleTimer(cardIdx);
        });
      });

      // Timer Reset button
      containerEl.querySelectorAll(".round-reset-btn").forEach(btn => {
        btn.addEventListener("click", (e) => {
          e.stopPropagation();
          const cardIdx = parseInt(btn.getAttribute("data-card"));
          stopTimer();
          const times = getTimes();
          times[cardIdx] = 300;
          updateView();
        });
      });

      // Adjusters (+1m / -1m)
      containerEl.querySelectorAll(".round-adjust-btn").forEach(btn => {
        btn.addEventListener("click", (e) => {
          e.stopPropagation();
          const cardIdx = parseInt(btn.getAttribute("data-card"));
          const delta = parseInt(btn.getAttribute("data-adjust"));
          const times = getTimes();
          times[cardIdx] = Math.max(30, times[cardIdx] + delta);
          const clockEl = containerEl.querySelector(`#${flowType}-clock-${cardIdx}`);
          if (clockEl) clockEl.textContent = formatTime(times[cardIdx]);
        });
      });

      // Click dimmed or completed card to activate directly
      containerEl.querySelectorAll(`.${cardBaseClass}.${cardPrefix}-card-dimmed, .${cardBaseClass}.${cardPrefix}-card-completed`).forEach(card => {
        card.addEventListener("click", (e) => {
          if (e.target.closest("button")) return;
          stopTimer();
          setActiveIndex(parseInt(card.getAttribute("data-index")));
          updateView();
        });
      });
    }

    function toggleTimer(cardIdx) {
      if (getRunningIndex() === cardIdx) {
        stopTimer();
        updateView();
      } else {
        stopTimer();
        setRunningIndex(cardIdx);
        const times = getTimes();
        const intervalHandle = setInterval(() => {
          if (times[cardIdx] > 0) {
            times[cardIdx]--;
            const clockEl = containerEl.querySelector(`#${flowType}-clock-${cardIdx}`);
            if (clockEl) {
              clockEl.textContent = formatTime(times[cardIdx]);
              if (times[cardIdx] === 0) {
                clockEl.classList.add("time-elapsed");
              }
            }
            if (times[cardIdx] === 0) {
              stopTimer();
              playChime();
              updateView();
            }
          } else {
            stopTimer();
            updateView();
          }
        }, 1000);
        setIntervalHandle(intervalHandle);
        updateView();
      }
    }

    // Initial render
    updateView();
  }

  // Break Slide (Morning, Lunch, Afternoon)
  function renderBreakCard(slide, containerEl) {
    containerEl.innerHTML = `
      <div class="break-center-container">
        <div class="break-glass-card">
          <div style="font-size: 3.5rem; margin-bottom: 12px;">☕ 🍽️</div>
          <h3 class="break-title">${slide.title}</h3>
          <p class="break-duration">${slide.duration}</p>
          <p class="break-sub">${slide.subtitle}</p>
          <div class="break-next-badge">
            ${slide.nextSession}
          </div>
        </div>
      </div>
    `;
  }

  // Strategy War Room 10 Matrix Headers
  function renderMatrixFramework(slide, containerEl) {
    const headersHtml = (slide.matrixHeaders || []).map((h, i) => `
      <div class="matrix-header-card">
        <span class="matrix-header-num">${i + 1}</span>
        <h4 class="matrix-header-title">${h.title}</h4>
        <p class="matrix-header-desc">${h.desc}</p>
      </div>
    `).join("");

    containerEl.innerHTML = `
      <div class="matrix-war-room-grid">
        ${headersHtml}
      </div>
    `;
  }

  // Generic fallback
  function renderGenericSlide(slide, containerEl) {
    containerEl.innerHTML = `
      <div style="padding: 40px; background: var(--card-bg); border-radius: 18px;">
        <h3 style="font-size: 2.2rem; color: #FFFFFF; margin-bottom: 15px;">${slide.title}</h3>
        <p style="font-size: 1.5rem; line-height: 1.6; color: var(--text-muted);">${slide.subtitle || ""}</p>
      </div>
    `;
  }

  // --------------------------------------------------------------------------
  // SPEAKER NOTES DRAWER
  // --------------------------------------------------------------------------
  function updateSpeakerNotes(slide) {
    if (!notesContent) return;
    notesContent.innerHTML = `
      <div class="notes-meta-badge">
        <i class="ri-bookmark-line"></i> Slide ${currentIndex + 1}: ${slide.category || ""}
      </div>
      <h4 style="font-family: 'Outfit'; font-size: 1.35rem; color: #FFFFFF; margin-bottom: 14px;">
        ${slide.title}
      </h4>
      <div style="background: rgba(255, 255, 255, 0.04); padding: 16px; border-radius: 10px; border-left: 3px solid var(--brand-orange); margin-bottom: 20px;">
        <span style="font-size: 0.8rem; font-weight: 800; color: var(--brand-orange); text-transform: uppercase;">Facilitator Directives</span>
        <p style="font-size: 1.1rem; line-height: 1.6; color: var(--text-main); margin-top: 6px;">
          ${slide.notes || "No special instructions for this slide."}
        </p>
      </div>
      <div style="display: flex; gap: 8px; flex-wrap: wrap;">
        <span class="filter-chip"><i class="ri-time-line"></i> Session: ${slide.session || "General"}</span>
        <span class="filter-chip"><i class="ri-user-voice-line"></i> Focus: Discussion</span>
      </div>
    `;
  }

  function toggleNotes() {
    notesDrawer.classList.toggle("active");
    btnNotes.classList.toggle("active");
  }

  // --------------------------------------------------------------------------
  // SIDEBAR AGENDA
  // --------------------------------------------------------------------------
  function buildSidebarList() {
    if (!sidebarSlidesList) return;
    sidebarSlidesList.innerHTML = "";

    slides.forEach((s, idx) => {
      if (activeFilterSession !== "all" && s.session !== activeFilterSession) {
        return;
      }
      const item = document.createElement("div");
      item.className = `slide-nav-item ${idx === currentIndex ? 'active' : ''}`;
      item.innerHTML = `
        <span class="slide-nav-num">${idx + 1}</span>
        <div class="slide-nav-meta">
          <span class="slide-nav-cat">${s.session || "Session"}</span>
          <span class="slide-nav-title">${s.title}</span>
        </div>
      `;

      item.addEventListener("click", () => {
        renderSlide(idx);
        closeSidebar();
      });

      sidebarSlidesList.appendChild(item);
    });
  }

  document.querySelectorAll(".sidebar-filter-tabs .filter-chip").forEach(chip => {
    chip.addEventListener("click", () => {
      document.querySelectorAll(".sidebar-filter-tabs .filter-chip").forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      activeFilterSession = chip.getAttribute("data-filter") || "all";
      buildSidebarList();
    });
  });

  function updateSidebarActiveState() {
    const items = sidebarSlidesList.querySelectorAll(".slide-nav-item");
    items.forEach((it, idx) => {
      const numSpan = it.querySelector(".slide-nav-num");
      if (numSpan && parseInt(numSpan.textContent) === currentIndex + 1) {
        it.classList.add("active");
      } else {
        it.classList.remove("active");
      }
    });
  }

  function openSidebar() {
    buildSidebarList();
    sidebar.classList.add("active");
    sidebarOverlay.classList.add("active");
  }

  function closeSidebar() {
    sidebar.classList.remove("active");
    sidebarOverlay.classList.remove("active");
  }

  // Top Session Nav Buttons
  function updateSessionNav(sessionName) {
    document.querySelectorAll("#session-nav .session-btn").forEach(btn => {
      const sess = btn.getAttribute("data-session");
      if (sess === "all") {
        btn.classList.remove("active");
      } else if (sess === sessionName) {
        btn.classList.add("active");
      } else {
        btn.classList.remove("active");
      }
    });
  }

  document.querySelectorAll("#session-nav .session-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const sess = btn.getAttribute("data-session");
      if (sess === "all") {
        renderSlide(0);
      } else {
        const targetIndex = slides.findIndex(s => s.session === sess || String(s.sessionNum) === sess);
        if (targetIndex !== -1) renderSlide(targetIndex);
      }
    });
  });

  // --------------------------------------------------------------------------
  // TIMER ENGINE (WEB AUDIO CHIME & DUAL-DISPLAY)
  // --------------------------------------------------------------------------
  function formatTime(seconds) {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  }

  function playChime() {
    try {
      const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.type = "sine";
      osc.frequency.setValueAtTime(587.33, audioCtx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 0.3);
      gain.gain.setValueAtTime(0.5, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 1.2);
      osc.start();
      osc.stop(audioCtx.currentTime + 1.2);
    } catch (e) {
      console.log("Audio not supported");
    }
  }

  function startTimer() {
    if (isTimerRunning) return;
    isTimerRunning = true;
    headerTimerBadge.style.display = "inline-flex";

    timerInterval = setInterval(() => {
      if (timerRemaining > 0) {
        timerRemaining--;
        updateAllTimerDisplays();
      } else {
        clearInterval(timerInterval);
        isTimerRunning = false;
        playChime();
        alert("⏱️ Discussion Time is Up!");
        updateAllTimerDisplays();
      }
    }, 1000);

    updateAllTimerDisplays();
  }

  function pauseTimer() {
    isTimerRunning = false;
    clearInterval(timerInterval);
    updateAllTimerDisplays();
  }

  function toggleTimer() {
    if (isTimerRunning) pauseTimer();
    else startTimer();
  }

  function resetTimer(seconds) {
    pauseTimer();
    timerDuration = seconds || timerDuration;
    timerRemaining = timerDuration;
    updateAllTimerDisplays();
  }

  function updateAllTimerDisplays() {
    const formatted = formatTime(timerRemaining);
    if (modalTimerDigits) modalTimerDigits.textContent = formatted;
    if (headerTimerDisplay) headerTimerDisplay.textContent = formatted;

    const slideTimerDigits = document.getElementById("slide-timer-digits");
    if (slideTimerDigits) slideTimerDigits.textContent = formatted;

    if (modalBtnStart) {
      modalBtnStart.innerHTML = isTimerRunning ? '<i class="ri-pause-fill"></i> Pause Timer' : '<i class="ri-play-fill"></i> Start Timer';
    }
  }

  window.setTimerPreset = function(sec) {
    resetTimer(sec);
    startTimer();
  };

  btnTimerModal.addEventListener("click", () => timerModal.classList.add("active"));
  btnCloseTimerModal.addEventListener("click", () => timerModal.classList.remove("active"));
  headerTimerBadge.addEventListener("click", () => timerModal.classList.add("active"));
  modalBtnStart.addEventListener("click", toggleTimer);
  modalBtnReset.addEventListener("click", () => resetTimer(300));

  // --------------------------------------------------------------------------
  // FULLSCREEN & AUTO-EXPAND ENGINE WITH TOP-NAV HOVER REVEAL
  // --------------------------------------------------------------------------
  const appHeader = document.getElementById("app-header");
  const topHoverZone = document.getElementById("top-nav-hover-zone");
  let headerHideTimeout = null;

  function updateFullscreenState() {
    const isFs = !!(document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.body.classList.contains("is-fullscreen"));
    if (isFs) {
      document.body.classList.add("is-fullscreen");
      btnFullscreen.innerHTML = '<i class="ri-fullscreen-exit-line"></i>';
      btnFullscreen.title = "Exit Fullscreen (F / Esc)";
    } else {
      document.body.classList.remove("is-fullscreen");
      btnFullscreen.innerHTML = '<i class="ri-fullscreen-line"></i>';
      btnFullscreen.title = "Toggle Fullscreen (F)";
      if (appHeader) appHeader.classList.remove("revealed");
    }
    scaleSlide();
    setTimeout(scaleSlide, 150);
    setTimeout(scaleSlide, 460);
  }

  document.addEventListener("fullscreenchange", updateFullscreenState);
  document.addEventListener("webkitfullscreenchange", updateFullscreenState);
  document.addEventListener("mozfullscreenchange", updateFullscreenState);

  function showFullscreenHeader() {
    if (!document.body.classList.contains("is-fullscreen")) return;
    clearTimeout(headerHideTimeout);
    if (appHeader) appHeader.classList.add("revealed");
  }

  function hideFullscreenHeaderDelayed() {
    if (!document.body.classList.contains("is-fullscreen")) return;
    clearTimeout(headerHideTimeout);
    headerHideTimeout = setTimeout(() => {
      if (appHeader) appHeader.classList.remove("revealed");
    }, 1200);
  }

  if (topHoverZone) {
    topHoverZone.addEventListener("mouseenter", showFullscreenHeader);
  }

  if (appHeader) {
    appHeader.addEventListener("mouseenter", showFullscreenHeader);
    appHeader.addEventListener("mouseleave", hideFullscreenHeaderDelayed);
  }

  document.addEventListener("mousemove", (e) => {
    if (!document.body.classList.contains("is-fullscreen")) return;
    if (e.clientY <= 55) {
      showFullscreenHeader();
    } else if (e.clientY > 85) {
      hideFullscreenHeaderDelayed();
    }
  });

  btnFullscreen.addEventListener("click", () => {
    if (!document.fullscreenElement && !document.webkitFullscreenElement) {
      if (document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen().catch(() => {
          document.body.classList.toggle("is-fullscreen");
          updateFullscreenState();
        });
      } else {
        document.body.classList.toggle("is-fullscreen");
        updateFullscreenState();
      }
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen().catch(() => {
          document.body.classList.remove("is-fullscreen");
          updateFullscreenState();
        });
      } else {
        document.body.classList.remove("is-fullscreen");
        updateFullscreenState();
      }
    }
  });

  // --------------------------------------------------------------------------
  // CONTROLS & EVENT LISTENERS
  // --------------------------------------------------------------------------
  function prevSlide() {
    if (currentIndex > 0) renderSlide(currentIndex - 1);
  }

  function nextSlide() {
    if (currentIndex < slides.length - 1) renderSlide(currentIndex + 1);
  }

  btnPrev.addEventListener("click", prevSlide);
  btnNext.addEventListener("click", nextSlide);

  btnPlay.addEventListener("click", () => {
    isAutoplayActive = !isAutoplayActive;
    if (isAutoplayActive) {
      playIcon.innerHTML = '<path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>';
      autoplayInterval = setInterval(() => {
        if (currentIndex < slides.length - 1) nextSlide();
        else {
          clearInterval(autoplayInterval);
          isAutoplayActive = false;
          playIcon.innerHTML = '<path d="M8 5v14l11-7z"/>';
        }
      }, 7000);
    } else {
      clearInterval(autoplayInterval);
      playIcon.innerHTML = '<path d="M8 5v14l11-7z"/>';
    }
  });

  btnNotes.addEventListener("click", toggleNotes);
  btnCloseNotes.addEventListener("click", () => notesDrawer.classList.remove("active"));

  btnToggleSidebar.addEventListener("click", openSidebar);
  btnCloseSidebar.addEventListener("click", closeSidebar);
  sidebarOverlay.addEventListener("click", closeSidebar);

  btnTheme.addEventListener("click", () => {
    currentTheme = (currentTheme === "dark") ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", currentTheme);
    btnTheme.innerHTML = (currentTheme === "dark") ? '<i class="ri-sun-line"></i>' : '<i class="ri-moon-line"></i>';
  });

  document.addEventListener("keydown", (e) => {
    if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;

    switch (e.key) {
      case "ArrowRight":
      case " ":
        e.preventDefault();
        nextSlide();
        break;
      case "ArrowLeft":
        e.preventDefault();
        prevSlide();
        break;
      case "n":
      case "N":
        toggleNotes();
        break;
      case "m":
      case "M":
        if (sidebar.classList.contains("active")) closeSidebar();
        else openSidebar();
        break;
      case "t":
      case "T":
        btnTheme.click();
        break;
      case "f":
      case "F":
        btnFullscreen.click();
        break;
      case "Escape":
        notesDrawer.classList.remove("active");
        timerModal.classList.remove("active");
        closeSidebar();
        break;
    }
  });

  const progressContainer = document.getElementById("progress-container");
  if (progressContainer) {
    progressContainer.addEventListener("click", (e) => {
      const rect = progressContainer.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const pct = clickX / rect.width;
      const target = Math.floor(pct * slides.length);
      renderSlide(target);
    });
  }

  // Initial Render Slide 0
  renderSlide(0);
});
