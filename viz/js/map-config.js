export const config = {
    type: 'choropleth',
    data: yourData, // Replace with your actual data object
    options: {
      scales: {
        projection: {
          axis: 'x',
          projection: 'albersUsa',
        },
        color: {
          axis: 'x',
          interpolate: v => (v < 0.5 ? 'green' : 'red'),
          legend: {
            position: 'bottom-right',
            align: 'right',
          },
        },
      },
    },
  };
  