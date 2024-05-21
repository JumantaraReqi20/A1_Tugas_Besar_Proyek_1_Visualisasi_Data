const ctx = document.getElementById("bar_wil_stok");
new Chart(ctx, {
    type: "bar",
    data: {
        labels: [
            "Red",
            "Blue",
            "Yellow",
            "Green",
            "Purple",
            "Orange"
        ],
        datasets: [
            {
                label: "# of Votes",
                data: [
                    12,
                    19,
                    3,
                    5,
                    2,
                    3
                ],
                borderWidth: 1
            }
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

//# sourceMappingURL=visualisasi.51d0597d.js.map
