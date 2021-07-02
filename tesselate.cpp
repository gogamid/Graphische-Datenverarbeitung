//
//  main.cpp
//  uebung3_D
//
//  Created by Yusuf Gördük on 30.05.21.
//

#include <iostream>
#include <vector>

/*
  Das konexe Polygon aus der Aufgabe
    - Die Aufteilung der Dreiecke fängt immer bei 0 an
    - untere Schleife ist genau darauf abgestimmt
    - geht index 0 immer startend auf die anderen Punkte um dreieck zu vervollständigen
 
 */
int* tessellate(int index[], int n)
{
    //std::vector<int> triangleCoords(((n - 2) * 3));
    std::vector<int>* triangleCoords = new std::vector<int>;
    for (int i = 1; i < n - 1; i++)
    {
        /*
        n = 5
        i = 3
        0, 1, 3
        0, 3, 4
        0, 4, 5
        */
        triangleCoords->push_back(index[0]);
        triangleCoords->push_back(index[i]);
        triangleCoords->push_back(index[i + 1]);
    }
    return triangleCoords->data();
}


int main()
{
    int size = 5;
    int index[] = { 0, 1, 3, 4, 5 };
    float coords[] = { 1, 4.5 /*P0*/, 2.5, 1 /*P1*/, 4.5, 3 /*P2*/, 5, 1.5 /*P3*/, 6, 3.5 /*P4*/, 4, 5 /*P5*/, 2.5, 3.5 /*P6*/ };
    int* triangles = tessellate(index, sizeof(index) / sizeof(index[0]));
    // size_t lengthOfTriangle = sizeof(triangles) / sizeof(triangles[0]);
    
    for (int i = 0; i < 9; i++)
    {
        if(triangles[i] == 0){
            printf("----- The triangle points: ----- \n");
        }
        std::cout << triangles[i] << " (" << coords[triangles[i] * 2] << ", " << coords[triangles[i] * 2 + 1] << ")" << std::endl;

    }
    
    printf("%d %d \n", sizeof(index) / sizeof(index[0]), sizeof(triangles) / sizeof(*triangles));
    /*
    0: 1.0, 4.5 -> 0, 1
    1: 2.5, 1.0 -> 2, 3
    3: 5.0, 1.5 -> 6, 7
    */
}
