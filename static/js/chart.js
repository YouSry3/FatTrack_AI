document.addEventListener('DOMContentLoaded', function() {
  const fatPercentage = parseFloat(document.querySelector('.percentage').textContent);
  
  // تحديد لون الفئة
  let category, color;
  if (fatPercentage < 6) {
      category = "Essential Fat";
      color = '#36b9cc';
  } else if (fatPercentage < 14) {
      category = "Athletic";
      color = '#1cc88a';
  } else if (fatPercentage < 18) {
      category = "Fitness";
      color = '#f6c23e';
  } else if (fatPercentage < 25) {
      category = "Average";
      color = '#f8a427';
  } else {
      category = "Obese";
      color = '#e74a3b';
  }

  // إنشاء المخطط
  const ctx = document.getElementById('fatChart').getContext('2d');
  new Chart(ctx, {
      type: 'doughnut',
      data: {
          labels: ['Body Fat', 'Lean Mass'],
          datasets: [{
              data: [fatPercentage, 100-fatPercentage],
              backgroundColor: [color, '#e9ecef'],
              borderWidth: 0
          }]
      },
      options: {
          responsive: true,
          plugins: {
              legend: {
                  position: 'bottom'
              },
              tooltip: {
                  callbacks: {
                      label: function(context) {
                          return `${context.label}: ${context.raw}%`;
                      }
                  }
              }
          },
          cutout: '70%'
      }
  });

  // عرض معلومات الفئات
  const categoriesInfo = document.getElementById('categoriesInfo');
  categoriesInfo.innerHTML = `
      <h3>Body Fat Categories</h3>
      <p>Your category: <strong>${category}</strong></p>
      <ul>
          <li><span style="color:#36b9cc">●</span> Essential Fat: <6%</li>
          <li><span style="color:#1cc88a">●</span> Athletic: 6-13%</li>
          <li><span style="color:#f6c23e">●</span> Fitness: 14-17%</li>
          <li><span style="color:#f8a427">●</span> Average: 18-24%</li>
          <li><span style="color:#e74a3b">●</span> Obese: 25%+</li>
      </ul>
  `;
});