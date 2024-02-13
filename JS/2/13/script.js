document.addEventListener("DOMContentLoaded", () => {

        // When the user clicks anywhere outside of the modal, close it

                // Get all modals, buttons, and close spans
        var modals = document.querySelectorAll(".modal");
        var buttons = document.querySelectorAll("button");
        var closeSpans = document.querySelectorAll(".close");

        // Function to open a modal by ID
        function openModal(modalId) {
            document.getElementById(modalId).style.display = "block";
        }

        // Function to close a modal by ID
        function closeModal(modalId) {
            document.getElementById(modalId).style.display = "none";
        }

        // Event listeners for the initial buttons
        buttons.forEach(button => {
            if (button.id.startsWith("button")) { // Only attach to main buttons
                button.addEventListener('click', function () {
                    openModal(button.id.replace('button', 'modal'));
                });
            }
        });

        // Event listeners for modal switching buttons
        buttons.forEach(button => {
            if (button.dataset.targetModal) {
                button.addEventListener('click', function () {
                    // Find the current modal, close it
                    modals.forEach(modal => {
                        if (modal.style.display === "block") {
                            closeModal(modal.id);
                        }
                    });
                    // Open the target modal
                    openModal(button.dataset.targetModal);
                });
            }
        });

        // Event listeners for close spans
        closeSpans.forEach(span => {
            span.addEventListener('click', function () {
                closeModal(span.parentElement.parentElement.id);
            });
        });

})