import sqlite3
from flask import Flask, app, request, jsonify

app = Flask(__name__)

@app.route('/salvar_produto', methods=['POST'])
def salvar_produto():
    produtos = request.json

    con = sqlite3.connect('bot-python.db')
    cursor = con.cursor()

    try:
        cursor.execute("INSERT INTO Products ('nome_do_produto', 'descricao', 'categoria', 'codigo_do_produto', 'peso', 'dimensoes', 'preco', 'quantidade_em_estoque', 'data_de_validade', 'cor', 'tamanho', 'material', 'fabricante', 'pais_de_origem', 'observacoes', 'codigo_de_barras', 'localizacao_no_armazem') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
            produtos.get('nome_do_produto'),
            produtos.get('descricao'),
            produtos.get('categoria'),
            produtos.get('codigo_do_produto'),
            produtos.get('peso'),
            produtos.get('dimensoes'),
            produtos.get('preco'),
            produtos.get('quantidade_em_estoque'),
            produtos.get('data_de_validade'),
            produtos.get('cor'),
            produtos.get('tamanho'),
            produtos.get('material'),
            produtos.get('fabricante'),
            produtos.get('pais_de_origem'),
            produtos.get('observacoes'),
            produtos.get('codigo_de_barras'),
            produtos.get('localizacao_no_armazem'),
        ))
        con.commit()
        return "Produto salvo com sucesso", 200  # Resposta de sucesso
    except Exception as e:
        return f"Erro ao salvar o produto: {str(e)}", 500  # Resposta de erro
    finally:
        con.close()

if __name__ == '__main__':
    app.run(debug=True)
