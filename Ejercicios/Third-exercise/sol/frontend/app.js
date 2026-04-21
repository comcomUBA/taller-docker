const history = [];
const BACKEND = "http://localhost:5000";

async function sendMessage() {
  const input = document.getElementById("message-input");
  const btn = document.getElementById("send-btn");
  const message = input.value.trim();
  if (!message) return;

  addMessage("user", message);
  history.push({ role: "user", content: message });
  input.value = "";

  const thinking = addMessage("thinking", "Pensando...");
  btn.disabled = true;
  input.disabled = true;

  try {
    const res = await fetch(`${BACKEND}/api/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, history: history.slice(0, -1) })
    });

    const data = await res.json();
    thinking.remove();
    addMessage("assistant", data.response);
    history.push({ role: "assistant", content: data.response });
  } catch (e) {
    thinking.remove();
    addMessage("assistant", "Error al conectar con el backend.");
  }

  btn.disabled = false;
  input.disabled = false;
  input.focus();
}

function addMessage(role, content) {
  const messages = document.getElementById("messages");
  const div = document.createElement("div");
  div.className = `message ${role}`;
  div.textContent = content;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
  return div;
}
