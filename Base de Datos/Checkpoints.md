# Checkpoints
Para no tener que cargar el log de TODA la base de bdd que se creo en mar de ajo 94' usamos checkpoints.
Un punto de control (checkpoint) es una registro especial en el archivo de log que indica que indica que todos los ítems modificados hasta ese punto han sido almacenados en disco.

## Checkpoints inactivos 
La creación de un checkpoint inactivo en el log implica la suspensión momentánea de todas las transacciones para hacer el volcado (flush) de todos los buffers en memoria al disco.

## Checkpoints activos 
Para aminorar la pérdida de tiempo de ejecución en el volcado a disco puede utilizarse una técnica conocida como checkpointing activo (non-quiescent o fuzzy checkpointing), que utiliza dos tipos de registros de checkpoint: (BEGIN CKPT, tact) y(END CKPT), en donde tact es un listado de todas las transacciones que se encuentran activas (es decir, que aún no hicieron commit). El procedimiento varía según cada algoritmo de recuperación.
