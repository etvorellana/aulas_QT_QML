// LoginApp_00.qml

import QtQuick 2.5
import QtQuick.Window 2.5

Window {
    // Definir a Janela Principal 
    id: root  // o id
    visible: true 
    width: 250; height: 400 // o tamanho
    title: qsTr("Crachá") // o título da Janela

    Image {

        id: bck_img
        anchors.fill: parent
        fillMode: Image.Stretch
        source: "Imagens/modelo.png"
    }

    //Image {

        //usrImg = "Imagens/pessoa.png"

    //}
}
        
        