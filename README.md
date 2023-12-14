# MONITORAMENTO-DAS-FERRAMENTAS

Modelo de Cloud [Function](https://cloud.google.com/functions/docs/concepts/overview?hl=pt-br) para monitorar as ferramentas do ambiente GCP e notificar via webhook em canais no Teams ou Discord.


## Linguagem
Essa aplicação utiliza como linguagem o [Python 3.9](https://www.python.org/).


### Configuração prévia
Inicialmente, dentro do canal da sua equipe no Teams, configure um [webhook](https://learn.microsoft.com/pt-br/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=dotnet).


Com o webhook criado e o link dele em mãos, deploye a [function](https://cloud.google.com/functions/docs/deploy?hl=pt-br#console) configurando uma variável de ambiente "URL", tendo como valor o link do webhook criado anteriormente.


Com a function criada, crie um canal de [notificação](https://cloud.google.com/monitoring/support/notification-options?hl=pt-br#webhooks) de webhook no Google Cloud Platform e cole o link de acesso da function.


Para iniciar o monitoramento, é necessário criar uma Política de [Alerta](https://cloud.google.com/monitoring/alerts?hl=pt-br#create-alerting-policy).


Selecione a métrica que você deseja monitorar e qual será o gatilho para essa política.


No campo "Notificações e nome", selecione o canal de notificação que você criou anteriormente.


Com isso, a function já estará pronta e enviará notificações no canal do Teams quando o gatilho da política de alerta for desparado.


Os campos que aparecerão na mensagem poderão ser configurados dentro do código da function, assim como também é possível criar mais canais e métricas para separar as notificações por tipo de aplicação.


Quando tudo estiver funcionando, as mensagens recebidas no Teams terão um layout parecido com esse:


<p align="center">
<img src="https://uploaddeimagens.com.br/images/004/690/593/original/ExemploWebHook.png">
</p>