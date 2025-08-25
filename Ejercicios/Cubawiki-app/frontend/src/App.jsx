import { useEffect, useState } from "react";


function App() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState("");
  const [team, setTeam] = useState("");


  const fetchItems = async () => {
    const res = await fetch("http://localhost:5000/api/items");
    const data = await res.json();
    setItems(data);
  };


  useEffect(() => {
    fetchItems();
  }, []);


  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!name || !team) return;
    await fetch("http://localhost:5000/api/items", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, team }),
    });
    setName("");
    setTeam("");
    fetchItems();
  };


const handleDelete = async (id) => {
  await fetch(`http://localhost:5000/api/items/${id}`, { method: "DELETE" });
  fetchItems();
};


// Agrupar por equipo
const isEmpty = items.length === 0;
let teams;
if (!isEmpty) {
  teams = items.reduce((acc, item) => {
    acc[item.team] = acc[item.team] || [];
    acc[item.team].push(item);
    return acc;
  }, {});
} else {
  teams = []
}

return (
    <div className="centered-container">
      <h1 className="title">Registro de integrantes por equipo</h1>
      
      <form onSubmit={handleSubmit} className="form-container">
        <input
          type="text"
          placeholder="Nombre"
          value={name}
          onChange={(e) => {
            if (e.target.value.length <= 20) {
              setName(e.target.value);
            }
          }}
          className="form-input"
        />
        <select
          value={team}
          onChange={(e) => setTeam(e.target.value)}
          className="form-input"
        >
          <option value="">Seleccionar equipo</option>
          <option value="RoseTree">RoseTree</option>
          <option value="TopoSort">TopoSort</option>
          <option value="FloodMax">FloodMax</option>
        </select>
        <button className="submit-button" type="submit">
          Agregar
        </button>
      </form>

      <div className="teams-grid">
        {Object.entries(teams).map(([teamName, members]) => (
          <div key={teamName} className="team-card">
            <h2 className="team-title">Equipo: {teamName}</h2>
            <ul className="members-list">
              {members.map((m) => (
                <li key={m.id} className="member-item">
                  <div className="member-info">
                    <span className="member-name">{m.name}</span>
                    <span className="member-date">
                      ({new Date(m.created_at).toLocaleString()})
                    </span>
                  </div>
                  <button
                    onClick={() => handleDelete(m.id)}
                    className="delete-button"
                  >
                    borrar
                  </button>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;