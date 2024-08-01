document.addEventListener('DOMContentLoaded', function() {
    const reservationForm = document.getElementById('reservationForm');
    if (reservationForm) {
        reservationForm.addEventListener('submit', function(event) {
            const room = document.getElementById('room').value;
            const checkIn = document.getElementById('check_in').value;
            const checkOut = document.getElementById('check_out').value;
            if (!room || !checkIn || !checkOut) {
                event.preventDefault();
                const confirmationMessage = document.getElementById('confirmationMessage');
                confirmationMessage.textContent = 'Please fill out all fields.';
                confirmationMessage.style.color = 'red';
            }
        });
    }
});
