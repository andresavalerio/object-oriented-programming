import { Point } from './point'

export class Square {
  private ir: Point
  private il: Point
  private sr: Point
  private sl: Point

  constructor(ir: Point, il: Point, sr: Point, sl: Point) {
    this.ir = ir
    this.il = il
    this.sr = sr
    this.sl = sl
  }

  area() {
    return this.ir.distance(this.il) ** 2
  }
}