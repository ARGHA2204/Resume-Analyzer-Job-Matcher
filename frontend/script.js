async function analyze() {
    const fileInput = document.getElementById("resume");
    const jobDesc = document.getElementById("job_desc").value;
    const result = document.getElementById("result");

    if (!fileInput.files[0]) {
        alert("Please upload a resume");
        return;
    }

    let formData = new FormData();
    formData.append("resume", fileInput.files[0]);
    formData.append("job_desc", jobDesc);

    try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        result.innerText = "Score: " + data.score + "% | " + data.suggestion;

    } catch (error) {
        console.error(error);
        result.innerText = "Error connecting to backend";
    }
}