// keyApp_00.qml
import QtQuick 2.5

DarkSquare {
    id: root
    width: 400; height: 200
    GreenSquare {
        id: square
        x: 8; y: 8
    }
    focus: true
    Keys.onLeftPressed: {
        if (square.x > 8) 
            square.x -= 8
    }
    Keys.onRightPressed: {
        if (square.x < width - 8) 
            square.x += 8
    }
    Keys.onUpPressed: {
        if (square.y > 8) square.y -= 8
    }
    Keys.onDownPressed: {
        if (square.y < height - 8) 
            square.y += 8
    }
    Keys.onPressed: {
        switch(event.key) {
            case Qt.Key_Plus:
                square.scale += 0.2
                break;
            case Qt.Key_Minus:
                square.scale -= 0.2
                break;
        }
    }
}