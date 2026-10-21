// JavaScript Interaktif Kustom
document.addEventListener('DOMContentLoaded', function () {
    console.log("Sistem Informasi Toko Sepatu Siap!");

    const buyButtons = document.querySelectorAll('.btn-beli');
    buyButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const namaSepatu = this.getAttribute('data-nama');
            alert(`Sepatu "${namaSepatu}" telah ditambahkan ke keranjang belanja Anda!`);
        });
    });
});
