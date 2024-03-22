#include <bits/stdc++.h>
using namespace std;
#define INF 1000000

vector<vector<pair<int,int>>> Grafo;
vector<int> distancia;
vector<bool>procesados;

void dijkstra(int nodo){
    //Cola de prioridad (peso, nodo)
    priority_queue<pair<int,int>> q;
    distancia[nodo] = 0;
    q.push({0,nodo});

    while(!q.empty()){
        // a -> n鷐ero del nodo que estamos procesando
        int a = q.top().second;
        q.pop();
        //Revisar si el nodo ya se proceso
        if(procesados[a]) continue;
        procesados[a] = true;

        //ciclo para revisar adyacencias
        // u -> cada nodo adyacente al nodo a
        for(auto u : Grafo[a]){
            //b -> nodo adyacente y w -> peso
            int b = u.first, w=u.second;

            if(distancia[a]+w < distancia[b]){
                distancia[b] = distancia[a]+w;
                q.push({-distancia[b],b});
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n,m,nodo_inicio=1;
    cin >> n >> m;

    //Inicializar el grafo
    Grafo.assign(n+1,vector<pair<int,int>>());
    distancia.assign(n+1,INF);
    procesados.assign(n+1,false);

    int u,v,p;

    for(int i=0;i<m;++i){
        cin >> u >> v >> p;
        Grafo[u].push_back({v,p});
        Grafo[v].push_back({u,p});
    }

    dijkstra(nodo_inicio);

    cout << "\nARREGLO DE DISTANCIAS\n";
    for(auto x : distancia){
        cout << x << " ";
    }

/*
5 6
1 2 5
1 4 9
1 5 1
5 4 2
4 3 6
3񁺐
*/

    return 0;
}
