'use client'
import { useEffect, useState } from 'react';
function App() {
  const [searchTerm, setSearchTerm] = useState("");
  const sampleData = [
    "Apple",
    "Banana",
    "Orange",
    "Grapes",
    "Strawberry",
    "Mango",
    "Pineapple",
    "Blueberry"
  ];
  const filteredData = sampleData.filter(item =>
    item.toLowerCase().includes(searchTerm.toLowerCase())
  );
  return (
    <div style={{ padding: "20px", maxWidth: "400px", margin: "0 auto" }}>
      <h1>Fruit List</h1>
      <input type="text" placeholder="Search fruits..." value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)} />
      <ul>
        {filteredData.length > 0 ? (
          filteredData.map((item, index) => <li key={index}>{item}</li>)
        ) : (
          <li>No results found.</li>
        )}
      </ul>
    </div>
  );
}
export default App;
