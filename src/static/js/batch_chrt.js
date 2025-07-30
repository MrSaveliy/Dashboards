document.addEventListener("DOMContentLoaded", function () {
  const container = document.getElementById('chart-container');
  if (!container) {
    console.error("Контейнер не найден");
    return;
  }

  let info;
  try {
    info = JSON.parse(container.dataset.batchInfo);
  } catch (e) {
    console.error("Ошибка парсинга JSON:", e);
    return;
  }

  if (!info || info.length === 0) {
    console.warn("Нет данных для отображения");
    return;
  }

  // --- Подготовка данных ---
  const data = info.map(item => {
    const [hours, minutes] = item.batch_time.split(":");
    const date = new Date(1970, 0, 1, parseInt(hours), parseInt(minutes));
    return {
      x: item.batch_date,
      y: date
    };
  });

  const thresholdTime = new Date(1970, 0, 1, 5, 0); // 5:00

  const ctx = document.getElementById('timeChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      datasets: [
        {
          label: 'Время выполнения батча',
          data: data,
          borderColor: 'rgb(75, 140, 220)',
          backgroundColor: 'rgba(75, 140, 220, 0.2)',
          pointRadius: 6,
          tension: 0.2
        },
        {
          label: 'Время SLA (5:00)',
          data: [],
          borderColor: 'rgba(255, 99, 132, 1)',
          borderDash: [5, 5],
          pointRadius: 0,
          fill: false
        }
      ]
    },
    options: {
      plugins: {
        legend: { position: 'top' },
        tooltip: {
          callbacks: {
            label: function(context) {
              const d = context.parsed;
              const date = new Date(d.y);
              const hours = date.getHours().toString().padStart(2, '0');
              const minutes = date.getMinutes().toString().padStart(2, '0');
              return `Время: ${hours}:${minutes}`;
            }
          }
        },
        annotation: {
          annotations: {
            line1: {
              type: 'line',
              yMin: thresholdTime,
              yMax: thresholdTime,
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 2,
            },
            box1: {
              type: 'box',
              yMin: new Date(1970, 0, 1, 3, 0),
              yMax: thresholdTime,
              backgroundColor: 'rgba(255, 99, 132, 0.15)',
              borderColor: 'transparent',
              label: {
                content: 'Время SLA',
                enabled: true,
                position: 'start',
                font: {
                  size: 12,
                  weight: 'bold'
                },
                color: 'rgba(255, 99, 132, 1)'
              }
            }
          }
        }
      },
      scales: {
        x: {
          type: 'time',
          time: {
            unit: 'day',
            displayFormats: { day: 'dd.MM.yyyy' },
            tooltipFormat: 'PP'
          },
          title: {
            display: true,
            text: 'Дата'
          }
        },
        y: {
          type: 'time',
          time: {
            unit: 'minute',
            displayFormats: { minute: 'HH:mm' }
          },
          title: {
            display: true,
            text: 'Время'
          },
          min: new Date(1970, 0, 1, 3, 0),
          max: new Date(1970, 0, 1, 7, 0),
          ticks: {
            stepSize: 20,
            callback: function(value) {
              const date = new Date(value);
              const hours = date.getHours().toString().padStart(2, '0');
              const minutes = date.getMinutes().toString().padStart(2, '0');
              return `${hours}:${minutes}`;
            }
          }
        }
      }
    }
  });
});