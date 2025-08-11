# ideas y posible estructura de la clase

## motivacion
ejemplos de uso real (librerías de python, dependencias de os, capaz algo que se pueda testear en el momento y se entienda).
no tenemos idea del nivel de experiencia de la gente que va a ir (hay que asumir que es 0), así que capaz sería interesante ir con algun programa medio armado y que tengan que modificar algo, o correrlo en algun sistema diferente (ej. windows, linux, mac) y que tengan que hacer algo con eso.

## estructura de la clase 
- Ejemplo de uso real
  - Presentación de un proyecto simple que utiliza contenedores
  - Explicación de cómo los contenedores facilitan el desarrollo y despliegue
- Introducción a la virtualización
  - Qué es la virtualización?
      Virtualization is a technology that allows you to create virtual, simulated environments from a single, physical machine.
      Through this process, IT professionals can make use out of their previous investments and optimize a physical machine’s full capacity by distributing resources that are traditionally bound to hardware across many different environments.
  - Beneficios de la virtualización
      + Cost savings: Improved hardware utilization can mean savings on additional physical resources, like hard drives or hard disks, as well as reducing the need for power, space, and cooling in the datacenter. With virtualization, multiple operating systems can run alongside each other and share the same virtualized hardware resources for optimized efficiency.
      + Isolated environments: Because they’re separated from the rest of a system, VMs won’t interfere with what’s running on the host hardware, and they are a good option for testing new applications or setting up a production environment.
      + Disaster recovery: VMs provide additional disaster recovery options by enabling failover that could previously only be achieved through additional hardware. Disaster recovery options reduce the time it takes to repair and set up the impacted server, leading to greater adaptability.
  - Tipos de virtualización
      + Server virtualization: server virtualization allows you to run multiple applications, each with its own VM and OS on a single physical server
      + Desktop virtualization: Desktop virtualization lets you run multiple desktop operating systems, each in its own VM on the same computer.
      +  Storage virtualization: Storage virtualization enables all the storage devices on the network, whether they’re installed on individual servers or stand-alone storage units, to be accessed and managed as a single storage device. Specifically, storage virtualization consolidates all blocks of storage into a single shared pool from which they can be assigned to any VM on the network as needed.
      + CPU virtualization: It allows a single CPU to be divided into multiple virtual CPUs for use by multiple VMs.
      +  Cloud virtualization: By virtualizing servers, storage and other physical data center resources, cloud computing providers can offer a range of services to customers, including the following: 
        Infrastructure as a service (IaaS): The delivery model IaaS provides a virtualized server, storage, and network resources you can configure based on their requirements.
        Platform as a service (PaaS): The PaaS service model offers virtualized development tools, databases and other cloud-based services that you can use to build your own cloud-based applications and solutions.
        Software as a service (SaaS): Software as a service refers to applications hosted on the cloud. SaaS is the most widely used cloud-based service.  

- Contenedores y Docker
  - Qué es un contenedor?
  - Introducción a Docker
  - Instalación de Docker
  - Primeros pasos con Docker: crear y ejecutar contenedores
- Desarrollo de aplicaciones en contenedores
  - Crear un Dockerfile
  - Construir, compartir y ejecutar imágenes de Docker
  - dockerhub
- Orquestación de contenedores
  - Introducción a Docker Compose
  - Definir y ejecutar aplicaciones multicontenedor (un montón pero capaz un ejemplo)

- sources
+ https://www.redhat.com/en/topics/virtualization/what-is-virtualization
+ https://www.ibm.com/think/topics/virtualization

### dudas
- nivel de interactividad/exposición
  - cuánto tiempo de exposición y cuánto de práctica?
  - qué tan interactivo? (ej. preguntas, ejercicios)
- qué tan avanzado?
- se van con algo hecho?
- que contenidos queremos que aprendan?