document.addEventListener("DOMContentLoaded", function () {

    const scanForm = document.getElementById("scanForm");
    const scanButton = document.getElementById("scanButton");

    if (scanForm && scanButton) {

        scanForm.addEventListener("submit", function () {

            const urlInput = document.getElementById("url");

            if (!urlInput.value.trim()) {
                return;
            }

            scanButton.disabled = true;

            scanButton.innerHTML = `
                <span class="loading-spinner"></span>
                Analyzing Website Security...
            `;

        });

    }

});