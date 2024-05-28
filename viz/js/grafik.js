$.getJSON("../stok_provinsi_advan.json", function (data) {
  const myChart =  new Chart(
      document.getElementById('bar_wil_stok'),
      {
        type: 'bar',
        data: {
          labels: data.map(row => row.Provinsi),
          datasets: [
            {
              label: 'Stok',
              data: data.map(row => row.Stok)
            }
          ]
        }
      }
    );
  console.log(data);
});