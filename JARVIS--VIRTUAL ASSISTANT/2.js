import { exec } from "child_process";

circle.addEventListener("click", () => {
  console.log("Button clicked");
  const pythonScript = "your-python-script.py";
  exec(`python ${pythonScript}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      terminal.innerHTML = `Error: ${error.message}`;
      return;
    }
    if (stderr) {
      console.error(`stderr: ${stderr}`);
      terminal.innerHTML = `Error: ${stderr}`;
      return;
    }
    terminal.innerHTML = stdout;
  });
});
