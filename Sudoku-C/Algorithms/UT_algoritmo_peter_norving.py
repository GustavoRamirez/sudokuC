import unittest
from peter_norving_algoritmo import peter_norving_algoritmo

class TestAlgoritmoPeter(unittest.TestCase):
    def setUp(self):
        self.filas = 'ABCDEFGHI'
        self.numeros = '123456789'
        self.juego_grid = "050807020600010090702540006070020301504000908103080070900076205060090003080103040"
        self.juego_grid_resuelto = "359867124648312597712549836876924351524731968193685472931476285465298713287153649"
        self.juego_dicc = {'I6': '3', 'H9': '3', 'I2': '8', 'E8': '6', 'H3': '5', 'H7': '7', 'I7': '6', 'I4': '1', 'H5': '9', 'F9': '2', 'G7': '2', 'G6': '6', 'G5': '7', 'E1': '5', 'G3': '1', 'G2': '3', 'G1': '9', 'I1': '2', 'C8': '3', 'I3': '7', 'E5': '3', 'I5': '5', 'C9': '6', 'G9': '5', 'G8': '8', 'A1': '3', 'A3': '9', 'A2': '5', 'A5': '6', 'A4': '8', 'A7': '1', 'A6': '7', 'C3': '2', 'C2': '1', 'C1': '7', 'E6': '1', 'C7': '8', 'C6': '9', 'C5': '4', 'C4': '5', 'I9': '9', 'D8': '5', 'I8': '4', 'E4': '7', 'D9': '1', 'H8': '1', 'F6': '5', 'A9': '4', 'G4': '4', 'A8': '2', 'E7': '9', 'E3': '4', 'F1': '1', 'F2': '9', 'F3': '3', 'F4': '6', 'F5': '8', 'E2': '2', 'F7': '4', 'F8': '7', 'D2': '7', 'H1': '4', 'H6': '8', 'H2': '6', 'H4': '2', 'D3': '6', 'B4': '3', 'B5': '1', 'B6': '2', 'B7': '5', 'E9': '8', 'B1': '6', 'B2': '4', 'B3': '8', 'D6': '4', 'D7': '3', 'D4': '9', 'D5': '2', 'B8': '9', 'B9': '7', 'D1': '8'}
        self.juego_dicc_resuelto = {'B8': '9', 'H1': '4', 'C7': '8', 'B3': '8', 'D3': '6', 'G9': '5', 'G8': '8', 'B9': '7', 'A3': '9', 'G7': '2', 'G6': '6', 'G5': '7', 'G4': '4', 'G3': '1', 'G2': '3', 'G1': '9', 'B5': '1', 'I1': '2', 'I3': '7', 'I2': '8', 'I5': '5', 'I4': '1', 'I7': '6', 'I6': '3', 'A1': '3', 'C9': '6', 'C8': '3', 'A5': '6', 'E8': '6', 'A7': '1', 'A6': '7', 'E5': '3', 'C2': '1', 'C1': '7', 'E6': '1', 'E1': '5', 'A2': '5', 'C5': '4', 'A4': '8', 'I9': '9', 'B2': '4', 'I8': '4', 'H2': '6', 'D9': '1', 'F2': '9', 'D5': '2', 'C3': '2', 'A9': '4', 'C6': '9', 'E4': '7', 'B1': '6', 'E7': '9', 'F1': '1', 'H8': '1', 'H9': '3', 'F4': '6', 'F5': '8', 'F6': '5', 'F7': '4', 'F8': '7', 'H3': '5', 'F3': '3', 'H6': '8', 'H7': '7', 'H4': '2', 'H5': '9', 'B4': '3', 'A8': '2', 'B6': '2', 'B7': '5', 'E9': '8', 'E3': '4', 'D8': '5', 'F9': '2', 'D6': '4', 'D7': '3', 'D4': '9', 'C4': '5', 'D2': '7', 'E2': '2', 'D1': '8'}
        self.new_instance = peter_norving_algoritmo()

    def test_verificar_que_metodo_cross_forma_un_cuadrado_de_9_x_9_con_digitos_y_rows(self):
        cuadrado = self.new_instance.cross(self.filas, self.numeros)
        cuadrado_pa_comparar = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
        self.assertEqual (cuadrado_pa_comparar, cuadrado)

    def test_verificar_juego_tenga_81_valores(self):
        assert len(self.new_instance.squares) == 81

    def test_verificar_juego_tenga_27_valores_para_unitlist(self):
        assert len(self.new_instance.unitlist) == 27

    def test_verificar_que_units_utilize_squares (self):
        assert all (len(self.new_instance.units[s]) == 3 for s in self.new_instance.squares)

    def test_verficar_que_peers_utilize_squares (self):
        assert all (len(self.new_instance.peers[s]) == 20 for s in self.new_instance.squares)

    def test_verificar_que_metodo_parse_grid_convierte_un_grid_en_un_diccionario(self):
        var_grid = self.new_instance.parse_grid (self.juego_grid)
        var_dicc = self.juego_dicc
        self.assertDictEqual (var_dicc, var_grid)

    def test_verificar_que_metodo_grid_values_convierte_un_solucion_en_diccionario(self):
        var_grid = self.new_instance.grid_values (self.juego_grid_resuelto)
        var_dicc = self.juego_dicc_resuelto
        self.assertDictEqual (var_dicc, var_grid)

    def test_verificar_que_metodo_solve_devuelve_una_solucion(self):
        var_grid = self.new_instance.grid_values (self.juego_grid_resuelto)
        var_dicc = self.juego_dicc_resuelto
        self.assertDictEqual (var_dicc, var_grid)

    def test_verificar_que_metodo_from_grid_agrupa_nueve_caracteres_y_pone_un_espaciador(self):
        var_grid_con_espacios = "050807020\n600010090\n702540006\n070020301\n504000908\n103080070\n900076205\n060090003\n080103040\n"
        var_grid = self.new_instance.from_grid(self.juego_grid)
        self.assertEqual (var_grid_con_espacios, var_grid)

    def test_verificar_que_metodo_resolvedor_conviernte_una_solucion_tipo_diccionario_a_una_solucion_tipo_cadena(self):
        var_grid = self.new_instance.resolvedor (self.juego_grid_resuelto)
        var_grid_resuelto = self.juego_grid_resuelto
        self.assertEqual (var_grid_resuelto,var_grid)

if __name__ == '__main__':
	unittest.main()
	pass


