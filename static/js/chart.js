class BodyFatAnalyzer {
  constructor() {
    this.fatPercentage = null;
    this.category = null;
    this.color = null;
    this.chart = null;
    
    this.init();
  }

  init() {
    this.getFatPercentage();
    this.determineCategory();
    this.renderChart();
    this.renderCategoryInfo();
    this.addEventListeners();
  }

  getFatPercentage() {
    const percentageText = document.querySelector('.percentage')?.textContent;
    this.fatPercentage = percentageText ? parseFloat(percentageText) : null;
  }

  determineCategory() {
    if (!this.fatPercentage || isNaN(this.fatPercentage)) return;

    const categories = [
      { max: 6, name: "Essential Fat", color: '#36b9cc', description: "Minimum essential fat for basic physiological functions" },
      { max: 14, name: "Athletic", color: '#1cc88a', description: "Typical for athletes and very fit individuals" },
      { max: 18, name: "Fitness", color: '#f6c23e', description: "Good fitness level, better than average" },
      { max: 25, name: "Average", color: '#f8a427', description: "Typical range for general population" },
      { max: Infinity, name: "Obese", color: '#e74a3b', description: "Higher than recommended levels" }
    ];

    this.category = categories.find(cat => this.fatPercentage < cat.max);
  }

  renderChart() {
    if (!this.fatPercentage || !this.category) return;

    const ctx = document.getElementById('fatChart')?.getContext('2d');
    if (!ctx) return;

    this.chart = new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: ['Body Fat', 'Lean Mass'],
        datasets: [{
          data: [this.fatPercentage, 100 - this.fatPercentage],
          backgroundColor: [this.category.color, '#e9ecef'],
          borderWidth: 0,
          hoverOffset: 10
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: {
              boxWidth: 12,
              padding: 20
            }
          },
          tooltip: {
            callbacks: {
              label: (context) => `${context.label}: ${context.raw}%`
            }
          }
        },
        cutout: '75%',
        animation: {
          animateScale: true,
          animateRotate: true
        }
      }
    });
  }

  renderCategoryInfo() {
    if (!this.category) return;

    const container = document.getElementById('categoriesInfo');
    if (!container) return;

    container.innerHTML = `
      <div class="category-card">
        <h3 class="category-title">Your Body Fat Analysis</h3>
        <div class="category-result" style="color: ${this.category.color}">
          ${this.category.name} (${this.fatPercentage}%)
        </div>
        <p class="category-description">${this.category.description}</p>

        <div class="category-scale">
          <h4>Body Fat Scale:</h4>
          <div class="scale-visual">
            ${this.renderScaleVisual()}
          </div>
          <ul class="scale-labels">
            <li><span class="dot" style="background:#36b9cc"></span> Essential Fat: &lt;6%</li>
            <li><span class="dot" style="background:#1cc88a"></span> Athletic: 6-13%</li>
            <li><span class="dot" style="background:#f6c23e"></span> Fitness: 14-17%</li>
            <li><span class="dot" style="background:#f8a427"></span> Average: 18-24%</li>
            <li><span class="dot" style="background:#e74a3b"></span> Obese: 25%+</li>
          </ul>
        </div>
      </div>
    `;
  }

  renderScaleVisual() {
    const ranges = [
      { max: 6, color: '#36b9cc' },
      { max: 14, color: '#1cc88a' },
      { max: 18, color: '#f6c23e' },
      { max: 25, color: '#f8a427' },
      { max: 100, color: '#e74a3b' }
    ];

    let currentPos = 0;
    let scaleHTML = '<div class="scale-bar">';

    ranges.forEach(range => {
      const width = range.max - currentPos;
      scaleHTML += `
        <div class="scale-segment" 
             style="width: ${width}%; background: ${range.color}"
             data-tooltip="${currentPos}-${range.max}%"></div>
      `;
      currentPos = range.max;
    });

    scaleHTML += `
      <div class="scale-marker" style="left: ${this.fatPercentage}%">
        <div class="marker-line"></div>
        <div class="marker-label">You</div>
      </div>
    `;

    scaleHTML += '</div>';
    return scaleHTML;
  }

  addEventListeners() {
    document.querySelectorAll('.scale-segment').forEach(segment => {
      segment.addEventListener('mouseover', (e) => {
        // Tooltip functionality placeholder
      });
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new BodyFatAnalyzer();
});
