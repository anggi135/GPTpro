const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

// Menentukan ukuran jaring
const width = 200;
const height = 200;

// Menentukan jumlah garis
const numLines = 10;

// Menentukan lebar garis
const lineWidth = 2;

// Menentukan warna garis
ctx.strokeStyle = "#000000";

// Menentukan jarak antar garis
const spacing = width / (numLines + 1);

// Menentukan posisi awal garis
let x = spacing;
let y = 0;

// Menggambar garis vertikal
for (let i = 0; i < numLines; i++) {
  ctx.moveTo(x, y);
  ctx.lineTo(x, y + height);
  ctx.stroke();
  x += spacing;
}

// Menentukan posisi awal garis
x = 0;
y = spacing;

// Menggambar garis horizontal
for (let i = 0; i < numLines; i++) {
  ctx.moveTo(x, y);
  ctx.lineTo(x + width, y);
  ctx.stroke();
  y += spacing;
}
