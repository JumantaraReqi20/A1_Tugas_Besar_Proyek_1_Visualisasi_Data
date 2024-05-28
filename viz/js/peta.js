// Assuming the TopoJSON is already loaded and showing the map

fetch('../stok_provinsi_advan.json')
  .then(response => response.json())
  .then(stokData => {
    // Create a mapping of province names to stock values
    const stokMap = stokData.reduce((acc, curr) => {
      acc[curr.Provinsi] = curr.Stok;
      return acc;
    }, {});

    fetch('../js/provinces-simplified-topo.json')
      .then(r => r.json())
      .then(indonesia => {
        const provinces = ChartGeo.topojson.feature(indonesia, indonesia.objects.provinces).features;

        const chart = new Chart(document.getElementById("canvas").getContext("2d"), {
          type: 'choropleth',
          data: {
            labels: provinces.map(d => d.properties.provinsi),
            datasets: [{
              label: 'Indonesian Provinces',
              outline: provinces,
              data: provinces.map(d => ({
                feature: d,
                value: stokMap[d.properties.provinsi] || 0,  // Use the stock value or 0 if not found
              })),
            }]
          },
          options: {
            plugins: {
              legend: {
                display: false
              },
            },
            scales: {
              projection: {
                axis: 'x',
                projection: 'mercator',
                interpolate: 'magma'
              },
              color: {
                axis: 'x',
                // quantize: 10,
                legend: {
                    length: 15000,
                    position: 'bottom-right',
                    align: 'right',
                },
              }
            },
          }
        });
      });
  });