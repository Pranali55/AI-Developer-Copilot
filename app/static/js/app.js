let uploadedCode = "";

// =============================
// DOM Elements
// =============================

const fileInput = document.getElementById("fileInput");
const uploadBtn = document.getElementById("uploadBtn");
const analyzeBtn = document.getElementById("analyzeBtn");

const codePreview = document.getElementById("codePreview");

const language = document.getElementById("language");
const lines = document.getElementById("lines");
const functionsCount = document.getElementById("functions");
const classesCount = document.getElementById("classes");
const comments = document.getElementById("comments");
const characters = document.getElementById("characters");

const loadingSpinner = document.getElementById("loadingSpinner");

const explanationResult = document.getElementById("explanationResult");
const reviewResult = document.getElementById("reviewResult");
const securityResult = document.getElementById("securityResult");
const documentationResult = document.getElementById("documentationResult");

const unitTestResult = document.getElementById("unitTestResult");

const targetLanguage = document.getElementById("targetLanguage");
const convertedCode = document.getElementById("convertedCode");

// =============================
// Helpers
// =============================

function showLoading() {
    loadingSpinner.style.display = "block";
}

function hideLoading() {
    loadingSpinner.style.display = "none";
}

function clearResults() {

    explanationResult.textContent =
        "Waiting for AI explanation...";

    reviewResult.textContent =
        "Waiting for AI review...";

    securityResult.textContent =
        "Waiting for AI security analysis...";

    documentationResult.textContent =
        "Waiting for AI documentation...";

    unitTestResult.textContent =
        "Waiting for AI unit tests...";

    convertedCode.textContent =
        "Converted code will appear here...";
}

// =============================
// Upload
// =============================

uploadBtn.addEventListener("click", async () => {

    if (fileInput.files.length === 0) {

        alert("Please select a source code file.");

        return;

    }

    const formData = new FormData();

    formData.append(
        "file",
        fileInput.files[0]
    );

    showLoading();

    try {

        const response = await fetch("/upload/", {

            method: "POST",

            body: formData

        });

        const data = await response.json();

        if (!response.ok) {

            hideLoading();

            alert(data.detail || "Upload failed.");

            return;

        }

        uploadedCode = data.code;

        language.textContent = data.language;
        lines.textContent = data.lines;
        functionsCount.textContent = data.functions;
        classesCount.textContent = data.classes;
        comments.textContent = data.comments;
        characters.textContent = data.characters;

        codePreview.textContent = data.code;

        analyzeBtn.disabled = false;

        clearResults();

        alert("Source code uploaded successfully.");

    }
    catch (error) {

        console.error(error);

        alert("Unable to upload file.");

    }
    finally {

        hideLoading();

    }

});

// =============================
// Analyze
// =============================

analyzeBtn.addEventListener("click", async () => {

    if (!uploadedCode) {

        alert("Please upload a file first.");

        return;

    }

    showLoading();

    try {

        // =============================
        // Explain
        // =============================

        let response = await fetch("/explain/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                code: uploadedCode
            })

        });

        let data = await response.json();

        explanationResult.textContent =
            data.explanation;

        // =============================
        // Review
        // =============================

        response = await fetch("/review/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                code: uploadedCode
            })

        });

        data = await response.json();

        reviewResult.textContent =
            data.review;

        // =============================
        // Security
        // =============================

        response = await fetch("/security/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                code: uploadedCode
            })

        });

        data = await response.json();

        securityResult.textContent =
            data.security;

        // =============================
        // Documentation Generator
        // =============================
                response = await fetch("/documentation/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                code: uploadedCode
            })

        });

        data = await response.json();

        documentationResult.textContent =
            data.documentation || "No documentation generated.";

        // =============================
        // Unit Test Generator
        // =============================

        response = await fetch("/tests/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                code: uploadedCode
            })

        });

        data = await response.json();

        unitTestResult.textContent =
            data.tests || "No unit tests generated.";

        // =============================
        // Code Converter
        // =============================

        response = await fetch("/convert/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                code: uploadedCode,

                target_language: targetLanguage.value

            })

        });

        data = await response.json();

        convertedCode.textContent =
            data.converted_code || "Conversion failed.";

    }
    catch (error) {

        console.error(error);

        alert("AI analysis failed. Check the browser console (F12) for details.");

    }
    finally {

        hideLoading();

    }

});