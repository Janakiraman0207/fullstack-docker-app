import React, { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/api/message")
      .then(res => res.json())
      .then(data => setMessage(data.message));
  }, []);

  return (
    <div style={{
      width: "100vw",
      height: "100vh",
      background: "#0f172a",
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      alignItems: "center",
      color: "white"
    }}>
      <h1>🔥 Full Stack Website</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
