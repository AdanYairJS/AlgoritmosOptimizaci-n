#include <bits/stdc++.h>
using namespace std;

struct Point{
	int x, y;
};

int orientation(Point p, Point q, Point r){
    // 0 --> puntos colineares
    // 1 --> horario
    // 2 --> antihorario
	int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
	if (val == 0) return 0;
	return (val > 0)? 1: 2;
}

void convexHull(Point points[], int n){
	vector<Point> hull;

	//Seleccionar el punto inicial (con la menor coordenada en x)
	int l = 0;
	for (int i = 1; i < n; i++)
		if (points[i].x < points[l].x)
			l = i;

	//ciclo hasta regresar al primer nodo
	//p -> nodo actual
	//q -> nodo auxiliar (siguiente nodo)
	int p = l, q;
	do{
		//Agregar el nodo actual al vector de índices finales
		hull.push_back(points[p]);

        //Seleccionar un valor inicial para q
		q = (p+1)%n;

		//Revisar el resto de nodos para encontrar el siguiente según la orientación
		// entre p, i y q
		for (int i = 0; i < n; i++){
            //Actualizar q por i en caso de que la combinación p->i->q->p sea antihoraria
            if (orientation(points[p], points[i], points[q]) == 2)
                q = i;
            }
        //El nuevo nodo actual será q
		p = q;

	} while (p != l); //Hasta regresar al nodo inicial

	hull.push_back(points[p]);

	//Imprimir el resultado
	for (int i = 0; i < hull.size(); i++)
		cout << "(" << hull[i].x << ", "
			<< hull[i].y << ")\n";

    //cout << "(" << hull[0].x << ", " << hull[0].y << ")\n";
}

int main()
{
    int n;
    cin >> n;
    Point points[n];
    for(int i=0;i<n;++i)
        cin >> points[i].x >> points[i].y;


	cout << "Coordenadas de los vertices de la envolvente convexa\n (En sentido antihorario)\n\n";
	convexHull(points, n);
	return 0;
}

/*
4
4 2 6 1 2 5 1 2

7
0 3 2 2 1 1 2 1 3 0 0 0 3 3
*/
