// Exemplo_01.qml

import QtQuick 2.14

// O elemento raiz é o retângulo
Rectangle {
    // nomeie este elemento como root
    id: root

    // atributos: <nome>: <valor>
    width: 120; height: 240  
    color: "#4A4A4A"

    // Declare um elemento aninhado (filho do raiz)
    Image {
        id: triangulo

        // referência ao pai
        x: (parent.width - width)/2 
        y: 40

        source: 'Imagens/triangle_red.png'
    }

    // Outro filho do root
    Text {
        // elemento sem nome

        // elemento referenciado pelo id
        y: triangulo.y + triangulo.height + 20

        // referencia ao elemento raiz
        width: root.width

        color: 'white'
        horizontalAlignment: Text.AlignHCenter
        text: 'Triângulo'
    }
}