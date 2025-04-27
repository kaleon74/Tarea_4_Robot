import pybullet as p
import pybullet_data
import time
import numpy as np
import os

# Configurar la ruta al archivo URDF
robot_urdf_path = "two_joint_robot_custom.urdf"

# Verificar que el archivo existe
if not os.path.exists(robot_urdf_path):
    print(f"ERROR: No se encuentra el archivo {robot_urdf_path}")
    print("Asegúrate de guardar el archivo URDF en la misma carpeta que este script")
    input("Presiona Enter para salir...")
    exit()

# Inicializar PyBullet
p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 1)

# Configurar la física y la cámara
p.setGravity(0, 0, -9.8)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.resetDebugVisualizerCamera(cameraDistance=1.5, cameraYaw=50, cameraPitch=-35, cameraTargetPosition=[0, 0, 0.5])

# Cargar el plano y el robot
planeId = p.loadURDF("plane.urdf")
print(f"Intentando cargar robot desde: {robot_urdf_path}")
robotId = p.loadURDF(robot_urdf_path, [0, 0, 0.1], useFixedBase=True)
print(f"Robot cargado con ID: {robotId}")

print("Simulación iniciada. El brazo se moverá automáticamente.")
print("Para mantener la ventana abierta, NO cierre este terminal.")

try:
    t = 0  # Tiempo simulado
    while True:
        # Movimiento automático usando seno y coseno
        joint1_value = np.sin(t) * (np.pi / 4)  # Oscila entre -45° y 45°
        joint2_value = np.cos(t) * (np.pi / 6)  # Oscila entre -30° y 30°

        # Controlar las articulaciones
        p.setJointMotorControl2(robotId, 0, p.POSITION_CONTROL, targetPosition=joint1_value, force=500)
        p.setJointMotorControl2(robotId, 2, p.POSITION_CONTROL, targetPosition=joint2_value, force=500)

        # Avanzar la simulación
        p.stepSimulation()
        time.sleep(1./240.)  # 240 FPS para que sea más suave

        # Avanzar el tiempo
        t += 0.01

except KeyboardInterrupt:
    print("Simulación interrumpida por el usuario")
finally:
    input("\nSimulación finalizada. Presiona Enter para cerrar completamente...")
    p.disconnect()
