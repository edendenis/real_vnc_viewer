#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `Real VNC Viewer` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `Real VNC Viewer` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/using the `Real VNC Viewer` on `Linux Ubuntu`._
# 

# ## Descrição [2]
# 
# ### `Real VNC Viewer`
# 
# O `Real VNC Viewer` é um cliente de acesso remoto que permite visualizar e controlar desktops de forma remota. Com ele, os usuários podem acessar computadores em diferentes plataformas e sistemas operacionais, como Windows, macOS e Linux, e interagir com eles como se estivessem fisicamente presentes. Ele oferece recursos avançados, como transferência de arquivos, chat e conexões criptografadas para garantir a segurança dos dados durante o acesso remoto. O `Real VNC Viewer` é uma ferramenta essencial para suporte técnico, administração de sistemas e trabalho remoto.
# 

# ## 1. Como configurar/instalar/usar o `Real VNC Viewer` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `Real VNC Viewer` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# Para instalar o `Real VNC Viewer` no `Linux Ubuntu` através do `Terminal Emulator`, siga os passos abaixo. Esses passos assumem que você está utilizando uma versão recente do `Ubuntu`. Caso esteja utilizando uma versão muito antiga ou muito específica, os comandos podem variar ligeiramente.
# 
# 3. **Instale o `Real VNC Viewe`r:** Após atualizar a lista de pacotes, você está pronto para instalar o `Real VNC Viewer`. Execute o comando: `sudo apt install realvnc-vnc-viewer -y`
# 
# Caso o pacote `realvnc-vnc-viewer` não esteja disponível nos repositórios padrão do `Ubuntu` (o que pode acontecer em versões específicas do `Ubuntu` ou em configurações personalizadas), você pode optar por baixar o instalador diretamente do site oficial do Real VNC e instalar manualmente. Aqui estão os passos para essa abordagem alternativa:
# 
# 1. **Baixe o pacote DEB:** Acesse o site oficial do Real VNC (`https://www.realvnc.com`) e procure pela seção de downloads do `VNC Viewer` para sistemas operacionais `Linux`. Baixe o arquivo .deb apropriado para a sua arquitetura (geralmente amd64 para sistemas modernos).
# 
# 2. **Instale o pacote DEB:** Após o _download_, você pode instalar o pacote usando o comando `dpkg`. Você precisará navegar até o diretório onde o arquivo foi baixado (geralmente `~/Downloads`) e então executar o comando: `sudo dpkg -i nome_do_pacote.deb`
# 
#     Substitua `nome_do_pacote.deb` pelo nome real do arquivo que você baixou.
# 
# 3. **Resolva dependências faltantes:** É possível que o comando `dpkg` indique a falta de dependências. Se isso acontecer, execute o comando: `sudo apt-get install -f`
# 
#     Isso irá automaticamente baixar e instalar quaisquer dependências faltantes.
# 
# Após a instalação, você pode iniciar o `VNC Viewer` através do menu de aplicações ou executando vncviewer no Terminal.
# 
# Lembre-se que para uma orientação mais específica ou atualizações sobre o processo de instalação, é sempre recomendado consultar a documentação oficial do software.

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `Real VNC Viewer` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean                                                            
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install realvnc-vnc-viewer -y
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Instalar real vnc: ubuntu.*** Disponível em: <https://chat.openai.com/c/c7e78146-272e-4009-97da-0ead9a652575> (texto adaptado). Acessado em: 03/04/2023 17:11.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 03/04/2024 17:10.
# 
