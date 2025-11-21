import pygame
import sys
import cx_Oracle

# =================== CONFIGURACIÓN ORACLE ===================
def registrar_resultado(jugador, puntaje_jugador, puntaje_cpu):
    try:
        conexion = cx_Oracle.connect("system", "Tapiero123", "localhost:1521/orcl")
        cursor = conexion.cursor()
        sql = """INSERT INTO JUEGO PINGPONG (JUGADOR, PUNTAJE_JUGADOR, PUNTAJE_CPU)
                VALUES (:1, :2, :3)"""  
        cursor.execute(sql, (jugador, puntaje_jugador, puntaje_cpu))
        conexion.commit()
        print("✔ Resultado registrado en Oracle")
    except Exception as e:
        print(f"❌ Error registrando resultado: {e}")
    finally:
        cursor.close()
        conexion.close()   

# =================== CONFIGURACIÓN DEL JUEGO ===================
pygame.init()
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ping Pong - Jugador vs CPU")

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Paddles
JUGADOR = pygame.Rect(50, ALTO//2 - 70, 10, 140)
CPU = pygame.Rect(ANCHO - 60, ALTO//2 - 70, 10, 140)
PELOTA = pygame.Rect(ANCHO//2 - 15, ALTO//2 - 15, 30, 30)

velocidad_pelota_x = 7
velocidad_pelota_y = 7
velocidad_jugador = 0
velocidad_cpu = 7

puntaje_jugador = 0
puntaje_cpu = 0
fuente = pygame.font.Font(None, 40)

clock = pygame.time.Clock()

# =================== BUCLE PRINCIPAL ===================
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            registrar_resultado("Jugador1", puntaje_jugador, puntaje_cpu)
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocidad_jugador = -7
            if event.key == pygame.K_DOWN:
                velocidad_jugador = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                velocidad_jugador = 0   

# Movimiento jugador    