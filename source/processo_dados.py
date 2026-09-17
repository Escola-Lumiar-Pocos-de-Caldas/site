# -*- coding: utf-8 -*-
"""Seção 'Como funciona na prática' — trilha do processo de projetos + caso real."""

FASES = [
    ('descobrir', 'Descobrir', 'Etapas 1 e 2', 'leaf',
     'Escutar cada estudante e achar a pergunta que move o ciclo inteiro.'),
    ('construir', 'Construir', 'Etapas 3 a 5', 'sun',
     'Transformar interesse em projeto com currículo, especialistas e plano.'),
    ('viver', 'Viver e avaliar', 'Etapas 6 e 7', 'navy',
     'Executar o trimestre, apresentar o resultado e avaliar por quatro ângulos.'),
]

CORES_FASE = {
    'leaf': dict(no='bg-leaf-500', txt='text-leaf-600', suave='bg-leaf-500/10',
                 anel='ring-leaf-500/25', chip='bg-leaf-500/12 text-leaf-600'),
    'sun':  dict(no='bg-sun-600',  txt='text-sun-700',  suave='bg-sun-600/10',
                 anel='ring-sun-600/25',  chip='bg-sun-600/10 text-sun-700'),
    'navy': dict(no='bg-navy-800', txt='text-navy-700', suave='bg-navy-800/8',
                 anel='ring-navy-800/20', chip='bg-navy-800/8 text-navy-700'),
}

ETAPAS = [
    dict(
        n='01', fase='leaf', dur='1 semana',
        etiqueta='Semana de Levantamento de Interesse',
        titulo='A gente começa perguntando.',
        texto='Antes de qualquer conteúdo, uma semana inteira dedicada a escutar. O tutor mapeia o que move cada estudante.',
        itens=['Roda de interesses com o ciclo inteiro',
               'Conversa individual entre tutor e estudante',
               'Cada interesse registrado no Mosaico'],
        caso_tit='O que o Miguel disse',
        caso='“Quero ser astronauta.” Miguel, 9 anos, perguntou na roda: <strong class="font-bold text-lumiar">como a pessoa dorme lá em cima sem cair da cama?</strong>',
    ),
    dict(
        n='02', fase='leaf', dur='Fim da 1ª semana',
        etiqueta='Interesse do Ciclo',
        titulo='Os interesses individuais viram uma pergunta coletiva.',
        texto='O tutor cruza os interesses de todos e busca o fio que conecta — não é votação, é a pergunta onde todo mundo cabe.',
        itens=['Agrupamento dos interesses por afinidade',
               'Pergunta norteadora construída junto com o ciclo',
               'Validação na Roda, com voz e voto dos estudantes'],
        caso_tit='A pergunta que o ciclo escolheu',
        caso='Miguel queria espaço; outros, corpo humano e robôs. O ciclo chegou junto em: <strong class="font-bold text-lumiar">“como viver fora da Terra?”</strong>',
    ),
    dict(
        n='03', fase='sun', dur='Semana 2',
        etiqueta='Nascem dois projetos',
        titulo='Um projeto do ciclo e um projeto individual — para cada estudante.',
        texto='Todo estudante participa do projeto coletivo e conduz também um projeto autoral só dele — currículo comum e único ao mesmo tempo.',
        itens=['<strong class="font-bold text-navy-800">Projeto do Ciclo</strong> — investigação coletiva, com entrega em grupo',
               '<strong class="font-bold text-navy-800">Projeto Individual</strong> — percurso autoral, um por estudante',
               'Os dois com propósito, objetivo e entregas definidos'],
        caso_tit='Os dois projetos do Miguel',
        caso='<span class="block"><strong class="font-bold text-lumiar">Do ciclo:</strong> projetar uma base habitável em Marte.</span><span class="mt-2 block"><strong class="font-bold text-lumiar">Individual:</strong> o que acontece com o corpo humano em gravidade zero?</span>',
    ),
    dict(
        n='04', fase='sun', dur='Semana 2',
        etiqueta='Plataforma Mosaico + BNCC',
        titulo='Aqui o sonho encontra o currículo obrigatório.',
        texto='Cada projeto entra no Mosaico e é cruzado com a BNCC. A plataforma mostra o que já cobre e o que falta — o tutor completa o resto.',
        itens=['Cada atividade vinculada a habilidades da BNCC',
               'As lacunas de currículo ficam visíveis para o tutor',
               'O percurso fica registrado e acompanhável pela família'],
        caso_tit='O que o projeto dele puxou da BNCC',
        caso='A dúvida sobre gravidade zero acabou cobrindo cinco áreas diferentes — sem nenhuma virar “matéria chata”.',
        pills=[('Ciências', 'Densidade, massa e corpo humano'),
               ('Matemática', 'Escala e proporção'),
               ('Língua Portuguesa', 'Relatório de pesquisa'),
               ('Geografia', 'Atmosfera e fusos'),
               ('Arte', 'Desenho técnico e maquete')],
    ),
    dict(
        n='05', fase='sun', dur='Semana 2 e 3',
        etiqueta='O tutor convoca os Mestres',
        titulo='Cada pedaço do projeto vai para quem é especialista naquilo.',
        texto='O tutor conhece o estudante e costura o percurso inteiro. Os mestres — professores especialistas — conduzem a parte de cada disciplina.',
        itens=['<strong class="font-bold text-navy-800">Tutor</strong> — acompanha o estudante e costura o projeto inteiro',
               '<strong class="font-bold text-navy-800">Mestres</strong> — licenciados que dão profundidade a cada área',
               'Oficinas e módulos abertos para todo o ciclo'],
        caso_tit='Quem entrou no projeto do Miguel',
        caso='A mestra de Matemática abriu oficina de escala para a maquete; a de Português orientou o relatório; Ciências trouxe um experimento de flutuação.',
    ),
    dict(
        n='06', fase='navy', dur='Trimestre inteiro',
        etiqueta='O plano do trimestre',
        titulo='Propósito, objetivo e plano — escritos, com data.',
        texto='Antes de começar, o projeto ganha um plano formal: por que existe, aonde quer chegar e o que será entregue — acompanhável no Mosaico.',
        itens=['<strong class="font-bold text-navy-800">Propósito</strong> — por que esse projeto importa para esse estudante',
               '<strong class="font-bold text-navy-800">Objetivo</strong> — o que ele vai aprender e produzir',
               '<strong class="font-bold text-navy-800">Plano</strong> — etapas, responsáveis e entregas do trimestre'],
        caso_tit='O combinado do trimestre',
        caso='Miguel fechou três entregas: um experimento de flutuação, uma maquete em escala e um relatório de quatro páginas.',
    ),
    dict(
        n='07', fase='navy', dur='Fim do trimestre',
        etiqueta='Culminância e avaliação integrada',
        titulo='Nada morre na gaveta. E ninguém é avaliado por um ângulo só.',
        texto='O trimestre fecha com apresentação pública do que foi produzido e uma avaliação sob quatro olhares diferentes.',
        itens=['<strong class="font-bold text-navy-800">Culminância</strong> — apresentação pública para turmas e famílias',
               '<strong class="font-bold text-navy-800">Avaliação integrada</strong> — habilidades da BNCC registradas no Mosaico',
               '<strong class="font-bold text-navy-800">Autoavaliação</strong> — o estudante analisa seu próprio percurso',
               '<strong class="font-bold text-navy-800">Devolutiva à família</strong> — conversa individual do tutor sobre o trimestre'],
        caso_tit='Como terminou',
        caso='Miguel apresentou a maquete para as turmas e famílias. Na autoavaliação, escreveu que o mais difícil foi acertar a escala — não o foguete.',
    ),
]

CHECK = ('<svg class="mt-[3px] h-4 w-4 shrink-0 %s" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>')


