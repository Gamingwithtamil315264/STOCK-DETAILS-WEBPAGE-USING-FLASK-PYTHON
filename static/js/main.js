  fetch('static/js/file.json')
  .then(response => response.json())
  .then(data => console.log(data)
  .catch(error => console.error('Error fetching JSON:', error));
const options = {
  container: document.getElementById("myChart"), // Container: HTML Element to hold the chart
  data:data,
  // Series: Defines which chart type and data to use
  series: [{ type: "line", xKey: data["Open"], yKey: data["Close"] }],
};

// Create Chart
agCharts.AgCharts.create(options);