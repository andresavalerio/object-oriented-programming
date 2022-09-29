import { Point } from './point'
import { Square } from './square'

describe('Square', () => {
  it('should calculate square area', () => {
    const ir = new Point(2, 0)
    const il = new Point(0, 0)
    const sr = new Point(2, 2)
    const sl = new Point(0, 2)
    const s1 = new Square(ir, il, sr, sl)
    expect(s1.area()).toEqual(4)
  })
})