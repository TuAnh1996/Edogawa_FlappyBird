var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
// để có thể thực hiện vẽ và nhiều thứu khác trên Canvas ta sd 
// Bây giờ, chúng ta cần tạo ra hình ảnh cho game Flappy Bird. Để tạo hình ảnh, chúng ta gán và hiển thị giá trị của hàm Image() bằng lệnh new.
var birdimg = new Image();
var hinhnenchinh = new Image();
var fg = new Image();
var ongtren = new Image();
var ongduoi = new Image();

var img = new Image();
// img.src = "images/over1.png";
img.src = "images/gameover.png";

// Tiếp theo, chúng ta phải thiết lập nguồn tải ảnh bằng thuộc tính src.
birdimg.src = "images/bird.png";
hinhnenchinh.src = "images/nenchinh.png";
fg.src = "images/fg1.png";
ongtren.src = "images/ongtren.png";
ongduoi.src = "images/ongduoi.png";

var fly = new Audio();
var scor = new Audio();

fly.src = "sounds/fly.mp3";
scor.src = "sounds/score.mp3";

// để tạo hiệu ứng rơi tự do cho chú chim và khoảng cách giữ hai uống nc chứng ngại vật 

var KhoangCachHaiOng = 150; //gap là khoảng cách giữa ống nước phía trên và ống nước phía dưới
var KhoangCachOngDuoi; //đẻ xac định tọa độ Y của ống nc phía dưới 
var bX = 30;
var bY = 150;

var gravity = 1.5;
// hàm gravity bằng 1.5, mỗi lần rơi chú chim sẽ rơi xuống 1.5 pixel
var score = 0;
document.addEventListener("keydown", moveUp);
// addEventListener tức khi mình ấn key thì nó chạy hàm moveUp
// keydown giúp ta nhấn vào bất cứ nút nào nó cũng chạy lên 25  bY -= 25;
// Tiếp theo, chúng ta cần tạo hoạt động bay lên cho chú chim mỗi khi bàn phím được nhấn. Người chơi có thể điểu khiển chú chim bằng cách nhấn phím bất kỳ trên bàn phím. Chúng ta cần thêm một biến EventListener vào code của mình và khi người chơi nhấn phím, chúng ta sẽ chạy hàm moveUp(), chú chim sẽ bay lên 25 pixel và phát ra hiệu ứng âm thanh.
function moveUp() {
    bY -= 25;
    fly.play();
}
// Chúng ta cũng cần lưu lại tọa độ của các ống nước bằng một mảng. Khi game khởi động, vị trí tọa độ X của các ống nước đầu tiên là 288 pixel (bằng cvs.width).
var ong = []; //tạo mảng ống để chứa các ống di chuỷen
ong[0] = {
    // x: canvas.width,
    x: canvas.width, //tức vị trí ban đầu là x= với width vd ở ddaay là 534 con rong 0
    y: 0 // khởi tạo ống đầu tiên nằm bên phải ngoài cùng và y=0;
}

function draw() {
    context.drawImage(hinhnenchinh, 0, 0);
    for (var i = 0; i < ong.length; i++) {
        KhoangCachOngDuoi = ongtren.height + KhoangCachHaiOng;
        context.drawImage(ongtren, ong[i].x, ong[i].y);
        context.drawImage(ongduoi, ong[i].x, ong[i].y + KhoangCachOngDuoi);
        // tạo tốc độ duy truyển của ống 
        ong[i].x -= 3; //để ống di chuyển t canvas.width / 2)
        if (ong[i].x == canvas.width - 300) { //tức sẽ tạo thêm thanh nữa nếu  (ong[i].x == 125)
            ong.push({
                x: canvas.width,
                y: Math.floor(Math.random() * ongtren.height) - ongtren.height
            });
        }
        if (bY <= 0 || bY + birdimg.height >= canvas.height - fg.height ||
            bX + birdimg.width >= ong[i].x && bX <= ong[i].x + ongtren.width &&
            (bY <= ong[i].y + ongtren.height ||
                bY + birdimg.height >= ong[i].y + KhoangCachOngDuoi)
        ) {
            // tức nó vào đây gặp thằng set nó nghỉ 1s xong nó thực hiện code trg đó sau khi thực hiện xong nó ms return nhớ phải cho return bên ngoài 
            setTimeout(function() {
                context.drawImage(img, 0, 0);
                context.fillStyle = '#000';
                context.font = "30px Verdana";
                context.fillText(" Score: " + score, 20, 50);
                //  reload() của đối tượng location được dùng để tải lại trang hiện tại.
            }, 500);
            return;
        }
        // location.reload(); //  reload() của đối tượng location được dùng để tải lại trang hiện tại.
        if (ong[i].x == 0) { //vì mình cho vtri con chim bằng 10 
            score++;
            scor.play(); // biến scor là biến tao ra nhạc tức khi ăn đc điểm thì tạo nhạc 
        }
    }
    context.drawImage(fg, 0, canvas.height - fg.height); //cái khung ở dưới x-0 còn y thì bằng cao của cvs trừ cái cao của khung
    context.drawImage(birdimg, bX, bY);
    bY += gravity;
    context.fillStyle = "#000";
    context.font = "20px Verdana";
    context.fillText("Score : " + score, 10, canvas.height - 20);
    requestAnimationFrame(draw); // giúp lăp đi lặp lại trg khoảng Tg gần gióng setTimeout  requestAnimationFrame sẽ vẽ lại nó liên tục.
    // alert("diem cua ban:" + score);
}
draw();