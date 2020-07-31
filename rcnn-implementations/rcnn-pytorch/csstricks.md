```

parent child {
    display: grid;
    place-items: center
}

wrapper parent {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

wrapper child {
    flex: 1 1 <basewidth> /* no stretching */
    flex: 0 1 <basewidth> /* stretching */
}

wrapper parent {
    display: grid;
    grid-template-columns: minmax(150px, 25%) 1fr;
}

```
