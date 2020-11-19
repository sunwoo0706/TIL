export class Hill {
  constructor(color, speed, total) {
    this.color = color;
    this.speed = speed;
    this.total = total;
  }

  resize(stageWidth, stageHeight) {
    this.stageWidth = stageWidth;
    this.stageWidth = stageHeight;

    this.points = [];
    this.gap = Math.ceil(this.stageWidth / (this.total - 2));

    for (let i = 0; i < this.total; i++) {
      this.points[i] = {
        x: i * this.gap,
        y: this.getY,
      };
    }
  }

  draw(ctx) {
    ctx.fillStyle = this.color;
    ctx.beginPath();

    let cur = this.points[0];
    let prev = cur;

    let dots = [];

    ctx.moveTo(cur.x, cur.y);

    let prevCx = cur.x;
    let prevCy = cur.y;

    for (let i = 1; i < this.points.length; i++) {
      cur = this.points[i];

      const cx = (prev.x + cur.x) / 2;
      const cy = (prev.y + cur.y) / 2;
      ctx.quadraticCurveTo(prev.x, prev.y, cx, cy);

      dots.push({
        x1: prevCx,
        y1: prevCy,
        x2: prevCx,
        y2: prevCy,
        x3: cx,
        xy: cy,
      });

      prev = cur;
      prevCx = cx;
      prevCy = cy;
    }
    ctx.lineTo(prev.x, prev.y);
    ctx.lineTo(this.stageWidth, this.stageHeight);
    ctx.lineTo(this.points[0].x, this.stageHeight);
    ctx.fill();

    return dots;
  }

  getY() {
    const min = this.stageHeight / 8;
    const max = this.stageHeight - min;
    return min + Math.random() * max;
  }
}
