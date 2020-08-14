```
<!-- center items -->
parent child {
    display: grid;
    place-items: center
}

<!-- deconstructed pancake -->
wrapper parent {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

wrapper child {
    flex: 1 1 <basewidth> /* no stretching */
    flex: 0 1 <basewidth> /* stretching */
}

<!-- sidebar with min size, stretching -->
wrapper parent {
    display: grid;
    grid-template-columns: minmax(150px, 25%) 1fr;
}

<!-- pancake stack -->
wrapper parent {
    display: grid;
    grid-template-rows: auto 1fr auto;
}

<!-- header, vertical stack, footer -->
wrapper parent {
    display: grid;
    grid-template: auto 1fr auto / autp 1fr auto;
}

wrapper header {
    grid-column: 1 / 4;
}

wrapper left-side {
    grid-column: 1 / 2;
}

wrapper main {
    grid-column: 2 / 3;
}

wrapper right-side {
    grid-column: 3 / 4;
}

wrapper footer {
    grid-column: 1 / 4;
}

<!-- 12 span grid -->
wrapper parent {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
}

wrapper span-12 {
    grid-column: 1 / 13;
}

wrapper span-6 {
    grid-column: 1 / 7;
}

wrapper span-4 {
    grid-column: 6 / 10;
}

<!-- RepeatAutoMinmax -->

wrapper parent {
    display: grid;
    grid-gap: 1em;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
}

<!-- line up -->
wrapper parent {
    height: auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}

wrapper visual {
    width: 100%;
    height: 100px;
}

wrapper card {
    display: flex;
    flex-direction: column;
    justify-content: space-between
}

<!-- clamp cards -->
wrapper parent {
    display: grid;
    place-items: center;
}

wrapper card {
    width: clamp(23ch, 50%, 46ch); <!-- character units-->
    display: flex;
    flex-direction: column;
}

wrapper visual {

}
```
