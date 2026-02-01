
import { useState } from "react";
import axios from "axios";

import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend
);

const chartOptions = {
  responsive: true,
  plugins: {
    legend: {
      labels: {
        color: "white",
        font: {
          size: 14,
        },
      },
    },
    tooltip: {
      enabled: true,
    },
  },
  scales: {
    x: {
      ticks: {
        color: "white",
        font: {
          size: 13,
        },
      },
      grid: {
        color: "#444",
      },
    },
    y: {
      beginAtZero: true,
      ticks: {
        color: "white",
        stepSize: 1,   // IMPORTANT: forces 0,1,2 not decimals
      },
      grid: {
        color: "#444",
      },
    },
  },
};

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [error, setError] = useState("");

  const chartData = result
  ? {
      labels: Object.keys(result.type_distribution),
      datasets: [
        {
          label: "Equipment Count",
          data: Object.values(result.type_distribution),
          backgroundColor: "#4ade80", // bright green
          borderRadius: 6,
        },
      ],

    }
  : null;

const login = async () => {
  try {
    const res = await axios.post("http://127.0.0.1:8000/api/token/", {
      username: "admin",
      password: "Adm1n1234" // USE EXACT PASSWORD YOU SET
    });

    localStorage.setItem("access", res.data.access);
    alert("Logged in successfully");
  } catch (err) {
    console.error(err);
    alert("Login failed — check username/password");
  }
};



  const handleUpload = async () => {
    const token = localStorage.getItem("access");

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post(
      "http://127.0.0.1:8000/api/upload/",
      formData,
      {
        headers: {
          "Authorization": `Bearer ${token}`,
          "Content-Type": "multipart/form-data"
        }
      }
    );

    setResult(res.data);
  };


  const fetchHistory = async () => {
    const res = await axios.get("http://127.0.0.1:8000/api/history/");
    setHistory(res.data);
  };

  return (
    <div style={{ padding: "30px", color: "white" }}>
      <h1>Chemical Equipment Visualizer</h1>

      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <br /><br />
      <button onClick={login}>Login</button>

      <button onClick={handleUpload}>Upload CSV</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div style={{ marginTop: "20px" }}>
          <button onClick={fetchHistory}>View Upload History</button>

          <h2>Summary</h2>
          <p>Total Equipment: {result.total_equipment}</p>
          <p>Average Flowrate: {result.avg_flowrate}</p>
          <p>Average Pressure: {result.avg_pressure}</p>
          <p>Average Temperature: {result.avg_temperature}</p>

          {result.pdf_report && (
            <div style={{ marginTop: "15px" }}>
              <button
                onClick={() => {
                  const token = localStorage.getItem("access");
                  const filename = result.pdf_report;

                  fetch(`http://127.0.0.1:8000/api/download/${filename}/`, {
                    headers: {
                      Authorization: `Bearer ${token}`,
                    },
                  })
                    .then((res) => res.blob())
                    .then((blob) => {
                      const url = window.URL.createObjectURL(blob);
                      const a = document.createElement("a");
                      a.href = url;
                      a.download = filename;
                      a.click();
                      window.URL.revokeObjectURL(url);
                    });
                }}
                style={{
                  marginTop: "15px",
                  background: "none",
                  border: "1px solid #4ade80",
                  color: "#4ade80",
                  padding: "8px 14px",
                  fontWeight: "bold",
                  cursor: "pointer",
                  borderRadius: "6px",
                }}
              >
                 Download PDF Report
              </button>

            </div>
          )}

          {chartData && (
            <>
              <h3>Type Distribution</h3>
              <div style={{ maxWidth: "500px" }}>
                <Bar data={chartData} options={chartOptions} />
              </div>
            </>
          )}

        </div>
      )}

      {history.length > 0 && (
        <div style={{ marginTop: "30px" }}>
          <h2>Upload History</h2>
          <ul>
            {history.map((item) => (
              <li key={item.id}>
                {item.uploaded_at} — Total: {item.total_equipment}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
