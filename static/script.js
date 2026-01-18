// ฟังก์ชันดึงค่าใหม่ทุก 1 วินาที (AJAX)
setInterval(function() {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            // Weather Data
            document.getElementById("t").innerText = data.temp;
            document.getElementById("h").innerText = data.humi;
            document.getElementById("p").innerText = data.pres;
            
            // Air Quality Data (PMS7003)
            document.getElementById("pm1").innerText = data.pm1;
            document.getElementById("pm25").innerText = data.pm25;
            document.getElementById("pm10").innerText = data.pm10;
            
            // Version
            document.getElementById("v").innerText = data.ver;
        })
        .catch(err => console.log(err));
}, 1000);