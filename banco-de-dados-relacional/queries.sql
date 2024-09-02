select count(*) as quantidade_livros from livro;

select nome as nome_cliente from Cliente order by nome;

select nome as editora, titulo as livro
from editora
inner join livro
on editora.idEditora = livro.idEditora
order by editora desc;

select editora.nome as editora, avg(livro.preco) as media_preco
from editora
inner join livro on editora.idEditora = livro.idEditora
group by editora;

select cliente.nome as nome_cliente, sum(itempedido.quantidade) as quantidade_livros
from cliente
inner join pedido on pedido.idCliente = cliente.idCliente
inner join itempedido on pedido.idPedido = itempedido.idPedido 
group by nome_cliente;