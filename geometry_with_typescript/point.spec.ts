import { Point } from './point'

describe('Point', () => {
  it('should create a point at the origin', () => {
    const p1: Point = new Point(0, 0)
  })

  it('should calculate distance between two points', () => {
    const p1: Point = new Point(0, 0)
    const p2: Point = new Point(0, 2)
    const d = p1.distance(p2)
    expect(d).toEqual(2)
  })
})