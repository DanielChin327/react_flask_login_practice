// src/components/Form.jsx
import { useState } from 'react';
import './Form.css'; // Import the CSS file

function Form() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  // Function to handle login
  const handleLogin = async (e) => {
    e.preventDefault();

    const response = await fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();
    alert(data.message);
  };

  // Function to handle registration
  const handleRegister = async (e) => {
    e.preventDefault();

    const response = await fetch('http://localhost:5000/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();
    alert(data.message);
  };

  return (
    <div className="form-container">
      <h2>Login</h2>
      <form className="form">
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <div className="button-group">
          <button onClick={handleLogin}>Login</button>
          <button onClick={handleRegister}>Register</button>
        </div>
      </form>
    </div>
  );
}

export default Form;
