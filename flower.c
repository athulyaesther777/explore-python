#include <graphics.h>
#include <conio.h>

void drawFlower() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\Turboc3\\BGI");

    // Draw the stem
    setcolor(GREEN);
    line(320, 400, 320, 300);

    // Draw the petals
    setcolor(RED);
    circle(320, 250, 50);
    circle(370, 250, 50);
    circle(270, 250, 50);
    circle(320, 200, 50);

    // Draw the center of the flower
    setcolor(YELLOW);
    setfillstyle(SOLID_FILL, YELLOW);
    fillellipse(320, 250, 30, 30);

    getch();
    closegraph();
}

int main() {
    drawFlower();
    return 0;
}
