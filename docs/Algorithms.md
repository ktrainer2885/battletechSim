# Algorithms

```mermaid 
flowchart LR

    subgraph Combat Algorithm
        start[Start]
        optimalRange[Optimal Range]
        movement[Movement]
        heat[Heat Profile]
        target[Choose Target]
        finish[Finish]
        shoot[Shoot]

        start --> target
        target --> heat
        heat --> optimalRange
        optimalRange --> movement
        movement --> shoot
        shoot --> finish
    end 
```