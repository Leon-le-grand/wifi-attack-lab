
// login.js - Demonstrating XSS and SQL Injection vulnerabilities

// --- XSS Vulnerability ---
// This function simulates displaying a username on the page.
// If the 'username' parameter contains malicious script, it will be executed.
function displayUsernameXSS() {
    const username = prompt("Enter your username for XSS test:");
    if (username) {
        // In a real application, this would be inserting into the DOM.
        // For demonstration, we'll just log it.
        // A vulnerable way would be: document.getElementById("usernameDisplay").innerHTML = username;
        console.log("Displaying username (XSS vulnerable): " + username);
        alert("XSS Vulnerable Display: " + username); // Simulating direct display
    }
}

// --- SQL Injection Vulnerability ---
// This function simulates a login check with a vulnerable SQL query construction.
// If 'username' or 'password' contain SQL special characters (e.g., ' OR 1=1--),
// the query can be manipulated.
function loginSQLi() {
    const username = prompt("Enter username for SQLi test:");
    const password = prompt("Enter password for SQLi test:");

    if (username && password) {
        // This is a highly vulnerable way to construct a SQL query.
        // NEVER do this in a real application. Use prepared statements.
        const sqlQuery = "SELECT * FROM users WHERE username = '' + username + '' AND password = '' + password + '';";
        console.log("Simulated SQL Query (SQL Injection vulnerable):");
        console.log(sqlQuery);
        alert("Simulated SQL Query (SQL Injection vulnerable):\n" + sqlQuery);
        // In a real application, this query would be executed against a database.
        // If SQLi is successful, an attacker could bypass authentication or extract data.
    }
}

// Call the functions to demonstrate
console.log("Running XSS demonstration...");
displayUsernameXSS();

console.log("\nRunning SQL Injection demonstration...");
loginSQLi();
