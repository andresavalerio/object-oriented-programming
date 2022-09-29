export class Point {
  private x: number
  private y: number
  
  constructor(x: number, y: number) {
    this.x = x
    this.y = y
  }

  distance(other: Point): number {
    const difX = this.x - other.x
    const difY = this.y - other.y

    return Math.sqrt(difX*difX + difY*difY)
  }
}