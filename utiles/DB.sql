--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO enredarteadmin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO enredarteadmin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO enredarteadmin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO enredarteadmin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO enredarteadmin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO enredarteadmin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO enredarteadmin;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO enredarteadmin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO enredarteadmin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO enredarteadmin;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO enredarteadmin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO enredarteadmin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: clientes_cliente; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.clientes_cliente (
    id integer NOT NULL,
    nombre character varying(64) NOT NULL,
    apellido character varying(64) NOT NULL,
    email character varying(254) NOT NULL,
    telefono character varying(64) NOT NULL,
    calle character varying(64) NOT NULL,
    numero character varying(6) NOT NULL,
    detalles text NOT NULL,
    localidad_id integer NOT NULL,
    fecha_creacion date NOT NULL
);


ALTER TABLE public.clientes_cliente OWNER TO enredarteadmin;

--
-- Name: compras_compra; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.compras_compra (
    id integer NOT NULL,
    detalles text NOT NULL,
    fecha_compra date NOT NULL,
    proveedor_id integer NOT NULL
);


ALTER TABLE public.compras_compra OWNER TO enredarteadmin;

--
-- Name: compras_compra_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.compras_compra_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.compras_compra_id_seq OWNER TO enredarteadmin;

--
-- Name: compras_compra_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.compras_compra_id_seq OWNED BY public.compras_compra.id;


--
-- Name: compras_insumoscompra; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.compras_insumoscompra (
    id integer NOT NULL,
    cantidad integer NOT NULL,
    compra_id integer NOT NULL,
    insumo_id integer NOT NULL,
    precio_compra integer NOT NULL,
    CONSTRAINT compras_insumoscompra_cantidad_check CHECK ((cantidad >= 0)),
    CONSTRAINT compras_insumoscompra_precio_compra_check CHECK ((precio_compra >= 0))
);


ALTER TABLE public.compras_insumoscompra OWNER TO enredarteadmin;

--
-- Name: compras_insumoscompra_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.compras_insumoscompra_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.compras_insumoscompra_id_seq OWNER TO enredarteadmin;

--
-- Name: compras_insumoscompra_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.compras_insumoscompra_id_seq OWNED BY public.compras_insumoscompra.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO enredarteadmin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO enredarteadmin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO enredarteadmin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO enredarteadmin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO enredarteadmin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO enredarteadmin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO enredarteadmin;

--
-- Name: gestion_cliente_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.gestion_cliente_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gestion_cliente_id_seq OWNER TO enredarteadmin;

--
-- Name: gestion_cliente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.gestion_cliente_id_seq OWNED BY public.clientes_cliente.id;


--
-- Name: gestion_localidad; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.gestion_localidad (
    id integer NOT NULL,
    localidad character varying(128) NOT NULL,
    provincia_id integer NOT NULL,
    cod_postal character varying(10) NOT NULL
);


ALTER TABLE public.gestion_localidad OWNER TO enredarteadmin;

--
-- Name: gestion_localidad_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.gestion_localidad_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gestion_localidad_id_seq OWNER TO enredarteadmin;

--
-- Name: gestion_localidad_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.gestion_localidad_id_seq OWNED BY public.gestion_localidad.id;


--
-- Name: gestion_provincia; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.gestion_provincia (
    id integer NOT NULL,
    cod_provincia character varying(10) NOT NULL,
    provincia character varying(50) NOT NULL
);


ALTER TABLE public.gestion_provincia OWNER TO enredarteadmin;

--
-- Name: gestion_provincia_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.gestion_provincia_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gestion_provincia_id_seq OWNER TO enredarteadmin;

--
-- Name: gestion_provincia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.gestion_provincia_id_seq OWNED BY public.gestion_provincia.id;


--
-- Name: pedidos_pedido; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.pedidos_pedido (
    id integer NOT NULL,
    precio_final numeric(6,2) NOT NULL,
    detalles text NOT NULL,
    estado character varying(64) NOT NULL,
    actualizado timestamp with time zone NOT NULL,
    fecha_pedido date NOT NULL,
    cliente_id integer NOT NULL
);


ALTER TABLE public.pedidos_pedido OWNER TO enredarteadmin;

--
-- Name: pedidos_pedido_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.pedidos_pedido_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pedidos_pedido_id_seq OWNER TO enredarteadmin;

--
-- Name: pedidos_pedido_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.pedidos_pedido_id_seq OWNED BY public.pedidos_pedido.id;


--
-- Name: pedidos_productospedido; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.pedidos_productospedido (
    id integer NOT NULL,
    cantidad integer NOT NULL,
    pedido_id integer NOT NULL,
    producto_id integer NOT NULL,
    CONSTRAINT pedidos_productospedido_cantidad_check CHECK ((cantidad >= 0))
);


ALTER TABLE public.pedidos_productospedido OWNER TO enredarteadmin;

--
-- Name: pedidos_productospedido_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.pedidos_productospedido_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pedidos_productospedido_id_seq OWNER TO enredarteadmin;

--
-- Name: pedidos_productospedido_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.pedidos_productospedido_id_seq OWNED BY public.pedidos_productospedido.id;


--
-- Name: productos_caracteristica; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.productos_caracteristica (
    id integer NOT NULL,
    nombre character varying(64) NOT NULL,
    detalles text NOT NULL
);


ALTER TABLE public.productos_caracteristica OWNER TO enredarteadmin;

--
-- Name: productos_caracteristica_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.productos_caracteristica_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.productos_caracteristica_id_seq OWNER TO enredarteadmin;

--
-- Name: productos_caracteristica_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.productos_caracteristica_id_seq OWNED BY public.productos_caracteristica.id;


--
-- Name: productos_caracteristicasproducto; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.productos_caracteristicasproducto (
    id integer NOT NULL,
    valor integer NOT NULL,
    caracteristica_id integer NOT NULL,
    producto_id integer NOT NULL,
    CONSTRAINT productos_caracteristicasproducto_valor_check CHECK ((valor >= 0))
);


ALTER TABLE public.productos_caracteristicasproducto OWNER TO enredarteadmin;

--
-- Name: productos_caracteristicasproducto_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.productos_caracteristicasproducto_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.productos_caracteristicasproducto_id_seq OWNER TO enredarteadmin;

--
-- Name: productos_caracteristicasproducto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.productos_caracteristicasproducto_id_seq OWNED BY public.productos_caracteristicasproducto.id;


--
-- Name: productos_insumo; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.productos_insumo (
    id integer NOT NULL,
    nombre character varying(64) NOT NULL,
    descripcion text NOT NULL,
    medida character varying(64) NOT NULL,
    precio numeric(6,2) NOT NULL,
    unidad_medida_id integer NOT NULL
);


ALTER TABLE public.productos_insumo OWNER TO enredarteadmin;

--
-- Name: productos_insumo_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.productos_insumo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.productos_insumo_id_seq OWNER TO enredarteadmin;

--
-- Name: productos_insumo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.productos_insumo_id_seq OWNED BY public.productos_insumo.id;


--
-- Name: productos_insumo_proveedores; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.productos_insumo_proveedores (
    id integer NOT NULL,
    insumo_id integer NOT NULL,
    proveedor_id integer NOT NULL
);


ALTER TABLE public.productos_insumo_proveedores OWNER TO enredarteadmin;

--
-- Name: productos_insumo_proveedores_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.productos_insumo_proveedores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.productos_insumo_proveedores_id_seq OWNER TO enredarteadmin;

--
-- Name: productos_insumo_proveedores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.productos_insumo_proveedores_id_seq OWNED BY public.productos_insumo_proveedores.id;


--
-- Name: productos_insumosproducto; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.productos_insumosproducto (
    id integer NOT NULL,
    cantidad integer NOT NULL,
    insumo_id integer NOT NULL,
    producto_id integer NOT NULL,
    CONSTRAINT productos_insumosproducto_cantidad_check CHECK ((cantidad >= 0))
);


ALTER TABLE public.productos_insumosproducto OWNER TO enredarteadmin;

--
-- Name: productos_insumosproducto_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.productos_insumosproducto_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.productos_insumosproducto_id_seq OWNER TO enredarteadmin;

--
-- Name: productos_insumosproducto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.productos_insumosproducto_id_seq OWNED BY public.productos_insumosproducto.id;


--
-- Name: productos_productimage; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.productos_productimage (
    id integer NOT NULL,
    imagen character varying(100) NOT NULL,
    producto_id integer NOT NULL
);


ALTER TABLE public.productos_productimage OWNER TO enredarteadmin;

--
-- Name: productos_productimage_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.productos_productimage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.productos_productimage_id_seq OWNER TO enredarteadmin;

--
-- Name: productos_productimage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.productos_productimage_id_seq OWNED BY public.productos_productimage.id;


--
-- Name: productos_producto; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.productos_producto (
    id integer NOT NULL,
    nombre character varying(128) NOT NULL,
    descripcion text NOT NULL,
    precio integer NOT NULL,
    CONSTRAINT productos_producto_precio_d84f7f62_check CHECK ((precio >= 0))
);


ALTER TABLE public.productos_producto OWNER TO enredarteadmin;

--
-- Name: productos_producto_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.productos_producto_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.productos_producto_id_seq OWNER TO enredarteadmin;

--
-- Name: productos_producto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.productos_producto_id_seq OWNED BY public.productos_producto.id;


--
-- Name: productos_stockinsumo; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.productos_stockinsumo (
    id integer NOT NULL,
    cantidad numeric(5,2) NOT NULL,
    detalles text NOT NULL,
    insumo_id integer NOT NULL
);


ALTER TABLE public.productos_stockinsumo OWNER TO enredarteadmin;

--
-- Name: productos_stockinsumo_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.productos_stockinsumo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.productos_stockinsumo_id_seq OWNER TO enredarteadmin;

--
-- Name: productos_stockinsumo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.productos_stockinsumo_id_seq OWNED BY public.productos_stockinsumo.id;


--
-- Name: productos_unidad; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.productos_unidad (
    id integer NOT NULL,
    nombre character varying(128) NOT NULL,
    descripcion text NOT NULL
);


ALTER TABLE public.productos_unidad OWNER TO enredarteadmin;

--
-- Name: productos_unidad_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.productos_unidad_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.productos_unidad_id_seq OWNER TO enredarteadmin;

--
-- Name: productos_unidad_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.productos_unidad_id_seq OWNED BY public.productos_unidad.id;


--
-- Name: proveedores_proveedor; Type: TABLE; Schema: public; Owner: enredarteadmin
--

CREATE TABLE public.proveedores_proveedor (
    id integer NOT NULL,
    cuit character varying(13) NOT NULL,
    razon_social character varying(64) NOT NULL,
    telefono character varying(64) NOT NULL,
    email character varying(254) NOT NULL,
    calle character varying(64) NOT NULL,
    numero character varying(4) NOT NULL,
    detalles text NOT NULL,
    localidad_id integer NOT NULL
);


ALTER TABLE public.proveedores_proveedor OWNER TO enredarteadmin;

--
-- Name: proveedores_proveedor_id_seq; Type: SEQUENCE; Schema: public; Owner: enredarteadmin
--

CREATE SEQUENCE public.proveedores_proveedor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proveedores_proveedor_id_seq OWNER TO enredarteadmin;

--
-- Name: proveedores_proveedor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: enredarteadmin
--

ALTER SEQUENCE public.proveedores_proveedor_id_seq OWNED BY public.proveedores_proveedor.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: clientes_cliente id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.clientes_cliente ALTER COLUMN id SET DEFAULT nextval('public.gestion_cliente_id_seq'::regclass);


--
-- Name: compras_compra id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.compras_compra ALTER COLUMN id SET DEFAULT nextval('public.compras_compra_id_seq'::regclass);


--
-- Name: compras_insumoscompra id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.compras_insumoscompra ALTER COLUMN id SET DEFAULT nextval('public.compras_insumoscompra_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: gestion_localidad id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.gestion_localidad ALTER COLUMN id SET DEFAULT nextval('public.gestion_localidad_id_seq'::regclass);


--
-- Name: gestion_provincia id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.gestion_provincia ALTER COLUMN id SET DEFAULT nextval('public.gestion_provincia_id_seq'::regclass);


--
-- Name: pedidos_pedido id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.pedidos_pedido ALTER COLUMN id SET DEFAULT nextval('public.pedidos_pedido_id_seq'::regclass);


--
-- Name: pedidos_productospedido id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.pedidos_productospedido ALTER COLUMN id SET DEFAULT nextval('public.pedidos_productospedido_id_seq'::regclass);


--
-- Name: productos_caracteristica id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_caracteristica ALTER COLUMN id SET DEFAULT nextval('public.productos_caracteristica_id_seq'::regclass);


--
-- Name: productos_caracteristicasproducto id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_caracteristicasproducto ALTER COLUMN id SET DEFAULT nextval('public.productos_caracteristicasproducto_id_seq'::regclass);


--
-- Name: productos_insumo id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumo ALTER COLUMN id SET DEFAULT nextval('public.productos_insumo_id_seq'::regclass);


--
-- Name: productos_insumo_proveedores id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumo_proveedores ALTER COLUMN id SET DEFAULT nextval('public.productos_insumo_proveedores_id_seq'::regclass);


--
-- Name: productos_insumosproducto id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumosproducto ALTER COLUMN id SET DEFAULT nextval('public.productos_insumosproducto_id_seq'::regclass);


--
-- Name: productos_productimage id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_productimage ALTER COLUMN id SET DEFAULT nextval('public.productos_productimage_id_seq'::regclass);


--
-- Name: productos_producto id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_producto ALTER COLUMN id SET DEFAULT nextval('public.productos_producto_id_seq'::regclass);


--
-- Name: productos_stockinsumo id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_stockinsumo ALTER COLUMN id SET DEFAULT nextval('public.productos_stockinsumo_id_seq'::regclass);


--
-- Name: productos_unidad id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_unidad ALTER COLUMN id SET DEFAULT nextval('public.productos_unidad_id_seq'::regclass);


--
-- Name: proveedores_proveedor id; Type: DEFAULT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.proveedores_proveedor ALTER COLUMN id SET DEFAULT nextval('public.proveedores_proveedor_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add cliente	1	add_cliente
2	Can change cliente	1	change_cliente
3	Can delete cliente	1	delete_cliente
4	Can view cliente	1	view_cliente
5	Can add estado pedido	2	add_estadopedido
6	Can change estado pedido	2	change_estadopedido
7	Can delete estado pedido	2	delete_estadopedido
8	Can view estado pedido	2	view_estadopedido
9	Can add insumo	3	add_insumo
10	Can change insumo	3	change_insumo
11	Can delete insumo	3	delete_insumo
12	Can view insumo	3	view_insumo
13	Can add insumos producto	4	add_insumosproducto
14	Can change insumos producto	4	change_insumosproducto
15	Can delete insumos producto	4	delete_insumosproducto
16	Can view insumos producto	4	view_insumosproducto
17	Can add localidad	5	add_localidad
18	Can change localidad	5	change_localidad
19	Can delete localidad	5	delete_localidad
20	Can view localidad	5	view_localidad
21	Can add provincia	6	add_provincia
22	Can change provincia	6	change_provincia
23	Can delete provincia	6	delete_provincia
24	Can view provincia	6	view_provincia
25	Can add unidad	7	add_unidad
26	Can change unidad	7	change_unidad
27	Can delete unidad	7	delete_unidad
28	Can view unidad	7	view_unidad
29	Can add stock insumo	8	add_stockinsumo
30	Can change stock insumo	8	change_stockinsumo
31	Can delete stock insumo	8	delete_stockinsumo
32	Can view stock insumo	8	view_stockinsumo
33	Can add proveedor	9	add_proveedor
34	Can change proveedor	9	change_proveedor
35	Can delete proveedor	9	delete_proveedor
36	Can view proveedor	9	view_proveedor
37	Can add producto	10	add_producto
38	Can change producto	10	change_producto
39	Can delete producto	10	delete_producto
40	Can view producto	10	view_producto
41	Can add pedido	11	add_pedido
42	Can change pedido	11	change_pedido
43	Can delete pedido	11	delete_pedido
44	Can view pedido	11	view_pedido
45	Can add log entry	12	add_logentry
46	Can change log entry	12	change_logentry
47	Can delete log entry	12	delete_logentry
48	Can view log entry	12	view_logentry
49	Can add permission	13	add_permission
50	Can change permission	13	change_permission
51	Can delete permission	13	delete_permission
52	Can view permission	13	view_permission
53	Can add group	14	add_group
54	Can change group	14	change_group
55	Can delete group	14	delete_group
56	Can view group	14	view_group
57	Can add user	15	add_user
58	Can change user	15	change_user
59	Can delete user	15	delete_user
60	Can view user	15	view_user
61	Can add content type	16	add_contenttype
62	Can change content type	16	change_contenttype
63	Can delete content type	16	delete_contenttype
64	Can view content type	16	view_contenttype
65	Can add session	17	add_session
66	Can change session	17	change_session
67	Can delete session	17	delete_session
68	Can view session	17	view_session
69	Can add cliente	18	add_cliente
70	Can change cliente	18	change_cliente
71	Can delete cliente	18	delete_cliente
72	Can view cliente	18	view_cliente
73	Can add insumo	19	add_insumo
74	Can change insumo	19	change_insumo
75	Can delete insumo	19	delete_insumo
76	Can view insumo	19	view_insumo
77	Can add unidad	20	add_unidad
78	Can change unidad	20	change_unidad
79	Can delete unidad	20	delete_unidad
80	Can view unidad	20	view_unidad
81	Can add stock insumo	21	add_stockinsumo
82	Can change stock insumo	21	change_stockinsumo
83	Can delete stock insumo	21	delete_stockinsumo
84	Can view stock insumo	21	view_stockinsumo
85	Can add AbstractProduct	22	add_producto
86	Can change AbstractProduct	22	change_producto
87	Can delete AbstractProduct	22	delete_producto
88	Can view AbstractProduct	22	view_producto
89	Can add insumos producto	23	add_insumosproducto
90	Can change insumos producto	23	change_insumosproducto
91	Can delete insumos producto	23	delete_insumosproducto
92	Can view insumos producto	23	view_insumosproducto
93	Can add proveedor	24	add_proveedor
94	Can change proveedor	24	change_proveedor
95	Can delete proveedor	24	delete_proveedor
96	Can view proveedor	24	view_proveedor
97	Can add pedido	25	add_pedido
98	Can change pedido	25	change_pedido
99	Can delete pedido	25	delete_pedido
100	Can view pedido	25	view_pedido
101	Can add variante	26	add_variante
102	Can change variante	26	change_variante
103	Can delete variante	26	delete_variante
104	Can view variante	26	view_variante
105	Can add Imagen de Producto	27	add_productimage
106	Can change Imagen de Producto	27	change_productimage
107	Can delete Imagen de Producto	27	delete_productimage
108	Can view Imagen de Producto	27	view_productimage
109	Can add productos pedido	28	add_productospedido
110	Can change productos pedido	28	change_productospedido
111	Can delete productos pedido	28	delete_productospedido
112	Can view productos pedido	28	view_productospedido
113	Can add caracteristicas producto	29	add_caracteristicasproducto
114	Can change caracteristicas producto	29	change_caracteristicasproducto
115	Can delete caracteristicas producto	29	delete_caracteristicasproducto
116	Can view caracteristicas producto	29	view_caracteristicasproducto
117	Can add Caracteristica	30	add_caracteristica
118	Can change Caracteristica	30	change_caracteristica
119	Can delete Caracteristica	30	delete_caracteristica
120	Can view Caracteristica	30	view_caracteristica
121	Can add insumos compra	31	add_insumoscompra
122	Can change insumos compra	31	change_insumoscompra
123	Can delete insumos compra	31	delete_insumoscompra
124	Can view insumos compra	31	view_insumoscompra
125	Can add compra	32	add_compra
126	Can change compra	32	change_compra
127	Can delete compra	32	delete_compra
128	Can view compra	32	view_compra
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
3	pbkdf2_sha256$150000$JU3ZdSVHHDiC$qckq9gxADZh42sa7kRD1agyfsGn/6V0xq5QAdiYlXdI=	2019-07-11 21:13:57.035997-03	f	test				f	t	2019-07-11 21:13:08.638688-03
2	pbkdf2_sha256$150000$bWdQxc7QilZY$j8uNulvsQ6ah7gJRExDN92LsfuqeWpkEtRJ8z8IL+ws=	2019-08-12 15:02:07.611461-03	f	marco			marcorichetta@gmail.com	f	t	2019-07-11 20:19:47.235011-03
1	pbkdf2_sha256$150000$jWByehGeJB6W$wH2+zYro5AbnxPL+mYo/qtVHeHbW/Q8ItXDpUgVyUFI=	2019-09-10 23:02:32.893647-03	t	admin			marcorichetta@gmail.com	t	t	2019-07-03 16:59:26.472348-03
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: clientes_cliente; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.clientes_cliente (id, nombre, apellido, email, telefono, calle, numero, detalles, localidad_id, fecha_creacion) FROM stdin;
1	Marcelo Elvio	Richetta	mrichetta@hotmail.com	3534987654	Santa Fe	565		1149	2019-08-06
2	Marco	Richetta	marcorichetta@gmail.com	3534220065	Santa Fe	565		1149	2019-08-06
\.


--
-- Data for Name: compras_compra; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.compras_compra (id, detalles, fecha_compra, proveedor_id) FROM stdin;
\.


--
-- Data for Name: compras_insumoscompra; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.compras_insumoscompra (id, cantidad, compra_id, insumo_id, precio_compra) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2019-07-03 17:13:32.710455-03	1	Cordoba	1	[{"added": {}}]	6	1
2	2019-07-03 17:13:34.553249-03	1	Las Perdices	1	[{"added": {}}]	5	1
3	2019-07-03 17:13:37.845837-03	1	Marco Richetta	1	[{"added": {}}]	1	1
4	2019-07-04 14:30:30.03747-03	2	General Cabrera	1	[{"added": {}}]	5	1
5	2019-07-04 14:30:32.445873-03	2	AGRICOLA ELVIO RICHETTA S.A.	1	[{"added": {}}]	9	1
6	2019-07-04 17:10:20.980928-03	2	Buenos Aires	1	[{"added": {}}]	6	1
7	2019-07-04 17:11:14.87236-03	4	Avellaneda	1	[{"added": {}}]	5	1
8	2019-07-05 14:27:20.566246-03	1	Las Perdices	1	[{"added": {}}]	5	1
9	2019-07-05 17:13:25.354538-03	2	Las Perdices	1	[{"added": {}}]	5	1
10	2019-07-05 17:13:42.62196-03	2	Las Perdices	3		5	1
11	2019-07-05 18:20:46.312623-03	1	Marco Richetta	1	[{"added": {}}]	1	1
12	2019-07-05 18:21:43.425607-03	2	Natalia Vera	1	[{"added": {}}]	1	1
13	2019-07-05 18:29:49.057095-03	3	Melba Coceres	1	[{"added": {}}]	1	1
14	2019-07-05 18:31:41.214175-03	4	Matias Richetta	1	[{"added": {}}]	1	1
15	2019-07-05 18:32:48.428466-03	5	Marcelo Elvio Richetta	1	[{"added": {}}]	1	1
16	2019-07-05 19:27:49.344652-03	28	Latin Outdoor SA	3		9	1
17	2019-07-05 19:27:49.348496-03	27	GRUPO INVERSOR PUBLICITARIO SA	3		9	1
18	2019-07-05 19:27:49.351647-03	26	e.a. carnevale y cia s.a.	3		9	1
19	2019-07-05 19:27:49.354715-03	25	Junin TV S.A.	3		9	1
20	2019-07-05 19:27:49.358116-03	24	Red Celeste y Blanca S.A.	3		9	1
21	2019-07-05 19:27:49.361843-03	23	America TV S.A.	3		9	1
22	2019-07-05 19:27:49.365444-03	22	ATACAMA SA DE PUBLICIDAD	3		9	1
23	2019-07-05 19:27:49.369138-03	21	VIA PUBLICA CLAN S.A.	3		9	1
24	2019-07-05 19:27:49.372514-03	20	ALEMANN S.R.L.	3		9	1
25	2019-07-18 13:18:19.114512-03	1	Marcelo Elvio Richetta	1	[{"added": {}}]	18	1
26	2019-07-22 15:31:44.378711-03	1	cm	1	[{"added": {}}]	20	1
27	2019-07-22 15:32:28.699548-03	1	MDF-3 - Plancha de fibrofacil de 3mm de grosor.	1	[{"added": {}}]	19	1
28	2019-07-23 19:46:02.14961-03	2	U	1	[{"added": {}}]	20	1
29	2019-07-23 19:46:25.670351-03	2	Lija-80 - Lija 80 porosidad	1	[{"added": {}}]	19	1
30	2019-07-23 19:47:24.340589-03	3	Kg	1	[{"added": {}}]	20	1
31	2019-07-23 19:47:36.162259-03	3	Cola Vinílica	1	[{"added": {}}]	19	1
32	2019-07-23 19:47:54.067032-03	2	Bandeja 30*25*4 - Bandeja 30 l x 25 a x 4 h	1	[{"added": {}}, {"added": {"name": "insumos producto", "object": "5 de MDF-3            por cada Bandeja 30*25*4"}}, {"added": {"name": "insumos producto", "object": "2 de Lija-80            por cada Bandeja 30*25*4"}}, {"added": {"name": "insumos producto", "object": "1 de Cola Vin\\u00edlica            por cada Bandeja 30*25*4"}}]	22	1
33	2019-07-23 19:48:39.767117-03	1	Pedido #1	1	[{"added": {}}]	25	1
34	2019-07-24 22:57:26.837224-03	1	Bandeja 30*25*4	1	[{"added": {}}]	27	1
35	2019-07-24 23:11:51.208404-03	1	Bandeja 30*25*4	3		27	1
36	2019-07-24 23:12:01.47762-03	2	Bandeja 30*25*4	1	[{"added": {}}]	27	1
37	2019-07-25 19:25:34.640178-03	3	Bastidor 35*25 - 	1	[{"added": {}}, {"added": {"name": "insumos producto", "object": "45 de MDF-3            por cada Bastidor 35*25"}}, {"added": {"name": "insumos producto", "object": "2 de Lija-80            por cada Bastidor 35*25"}}, {"added": {"name": "insumos producto", "object": "5 de Cola Vin\\u00edlica            por cada Bastidor 35*25"}}]	22	1
38	2019-07-25 19:26:50.436788-03	3	Bastidor 35*25	1	[{"added": {}}]	27	1
39	2019-07-26 13:57:23.154146-03	4	Prueba - asabab	2	[{"added": {"name": "insumos producto", "object": "5 de MDF-3            por cada Prueba"}}, {"added": {"name": "insumos producto", "object": "2 de Lija-80            por cada Prueba"}}, {"added": {"name": "insumos producto", "object": "1 de Cola Vin\\u00edlica            por cada Prueba"}}]	22	1
40	2019-07-26 14:25:15.716072-03	4	Prueba	1	[{"added": {}}]	27	1
41	2019-07-26 14:25:38.5273-03	4	Prueba	3		27	1
42	2019-07-26 14:25:54.640526-03	5	Prueba	1	[{"added": {}}]	27	1
43	2019-07-26 20:13:14.549164-03	6	Variante object (6)	1	[{"added": {}}]	26	1
44	2019-07-26 20:49:17.869813-03	6	Variante object (6)	3		26	1
45	2019-07-26 20:49:17.884227-03	5	Variante object (5)	3		26	1
46	2019-07-26 20:49:17.897076-03	4	Variante object (4)	3		26	1
47	2019-07-26 20:49:17.909032-03	3	Variante object (3)	3		26	1
48	2019-07-26 22:13:45.700244-03	6	prueba 3 - asdasd	3		22	1
49	2019-07-26 22:13:45.721788-03	5	Nuevo Producto - Prueba 123123	3		22	1
50	2019-07-26 22:13:45.736956-03	4	Prueba - asabab	3		22	1
51	2019-07-31 20:45:13.557889-03	3	Bastidor 35*25 - 	3		22	1
52	2019-07-31 20:45:13.573115-03	2	Bandeja 30*25*4 - Bandeja 30 l x 25 a x 4 h	3		22	1
53	2019-07-31 20:45:13.587689-03	1	Bandeja - Bandeja de fibrofacil base	3		22	1
54	2019-07-31 20:52:58.260954-03	9	Prueba - asdasddas	1	[{"added": {}}, {"added": {"name": "insumos producto", "object": "3 de MDF-3            por cada Prueba"}}, {"added": {"name": "insumos producto", "object": "1 de Lija-80            por cada Prueba"}}, {"added": {"name": "insumos producto", "object": "5 de Cola Vin\\u00edlica            por cada Prueba"}}]	22	1
55	2019-08-01 10:47:57.762189-03	9	Prueba - asdasddas	3		22	1
56	2019-08-01 10:47:57.785958-03	8	Prueba - asdasdasd	3		22	1
57	2019-08-01 10:47:57.79994-03	7	Prueba - asdasdasd	3		22	1
58	2019-08-01 19:16:53.787359-03	10	Bandeja 30*25*4 - Bandeja de fibrofacil	1	[{"added": {}}, {"added": {"name": "insumos producto", "object": "5 de MDF-3            por cada Bandeja 30*25*4"}}, {"added": {"name": "insumos producto", "object": "1 de Lija-80            por cada Bandeja 30*25*4"}}, {"added": {"name": "insumos producto", "object": "2 de Cola Vin\\u00edlica            por cada Bandeja 30*25*4"}}]	22	1
59	2019-08-01 19:17:13.766881-03	5	Pedido #5	1	[{"added": {}}, {"added": {"name": "productos pedido", "object": "3 - Bandeja 30*25*4"}}]	25	1
60	2019-08-01 19:23:21.151404-03	11	Bastidor 35*25 - Bastidor de fibrofacil	1	[{"added": {}}, {"added": {"name": "insumos producto", "object": "5 de MDF-3            por cada Bastidor 35*25"}}, {"added": {"name": "insumos producto", "object": "3 de Lija-80            por cada Bastidor 35*25"}}, {"added": {"name": "insumos producto", "object": "2 de Cola Vin\\u00edlica            por cada Bastidor 35*25"}}]	22	1
61	2019-08-01 19:23:34.020069-03	5	Pedido #5	2	[{"changed": {"fields": ["precio_final"]}}, {"added": {"name": "productos pedido", "object": "2 - Bastidor 35*25"}}]	25	1
62	2019-08-01 22:30:24.709352-03	2	Marco Richetta	1	[{"added": {}}]	18	1
63	2019-08-02 19:21:12.684462-03	8	Pedido #8	1	[{"added": {}}, {"added": {"name": "productos pedido", "object": "4 - Bandeja 30*25*4"}}, {"added": {"name": "productos pedido", "object": "2 - Bastidor 35*25"}}]	25	1
64	2019-08-02 19:22:55.040476-03	8	Pedido #8	2	[{"changed": {"name": "productos pedido", "object": "3 - Bastidor 35*25", "fields": ["cantidad"]}}]	25	1
65	2019-08-06 22:23:55.662537-03	11	Pedido #11	2	[{"changed": {"fields": ["precio_final"]}}]	25	1
66	2019-08-07 17:54:07.467947-03	12	Reloj 30*30 - 	1	[{"added": {}}, {"added": {"name": "insumos producto", "object": "4 de MDF-3            por cada Reloj 30*30"}}, {"added": {"name": "insumos producto", "object": "2 de Lija-80            por cada Reloj 30*30"}}, {"added": {"name": "insumos producto", "object": "1 de Cola Vin\\u00edlica            por cada Reloj 30*30"}}]	22	1
67	2019-08-07 18:33:18.78442-03	2	NEGRETE S.A.	1	[{"added": {}}]	24	1
68	2019-08-07 18:33:42.679782-03	4	MDF-5 - FF 5mm	1	[{"added": {}}]	19	1
69	2019-08-09 11:46:59.68851-03	2	Largo	1	[{"added": {}}]	30	1
70	2019-08-09 11:47:13.267099-03	3	Ancho	1	[{"added": {}}]	30	1
71	2019-08-09 11:47:17.462878-03	4	Alto	1	[{"added": {}}]	30	1
72	2019-08-09 11:49:35.109547-03	2	Largo: 30	1	[{"added": {}}]	29	1
73	2019-08-09 11:50:11.284925-03	3	Ancho: 25	1	[{"added": {}}]	29	1
74	2019-08-09 11:50:19.269237-03	4	Alto: 4	1	[{"added": {}}]	29	1
75	2019-08-27 18:48:37.536914-03	10	Pedido #10	2	[{"changed": {"fields": ["detalles"]}}]	25	1
76	2019-08-27 18:48:57.212721-03	11	Pedido #11	2	[{"changed": {"fields": ["detalles"]}}]	25	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	gestion	cliente
2	gestion	estadopedido
3	gestion	insumo
4	gestion	insumosproducto
5	gestion	localidad
6	gestion	provincia
7	gestion	unidad
8	gestion	stockinsumo
9	gestion	proveedor
10	gestion	producto
11	gestion	pedido
12	admin	logentry
13	auth	permission
14	auth	group
15	auth	user
16	contenttypes	contenttype
17	sessions	session
18	clientes	cliente
19	productos	insumo
20	productos	unidad
21	productos	stockinsumo
22	productos	producto
23	productos	insumosproducto
24	proveedores	proveedor
25	pedidos	pedido
26	productos	variante
27	productos	productimage
28	pedidos	productospedido
29	productos	caracteristicasproducto
30	productos	caracteristica
31	compras	insumoscompra
32	compras	compra
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-07-03 16:58:21.564779-03
2	auth	0001_initial	2019-07-03 16:58:21.658633-03
3	admin	0001_initial	2019-07-03 16:58:21.826273-03
4	admin	0002_logentry_remove_auto_add	2019-07-03 16:58:21.870637-03
5	admin	0003_logentry_add_action_flag_choices	2019-07-03 16:58:21.886735-03
6	contenttypes	0002_remove_content_type_name	2019-07-03 16:58:21.914536-03
7	auth	0002_alter_permission_name_max_length	2019-07-03 16:58:21.925937-03
8	auth	0003_alter_user_email_max_length	2019-07-03 16:58:21.940442-03
9	auth	0004_alter_user_username_opts	2019-07-03 16:58:21.952864-03
10	auth	0005_alter_user_last_login_null	2019-07-03 16:58:21.967299-03
11	auth	0006_require_contenttypes_0002	2019-07-03 16:58:21.970868-03
12	auth	0007_alter_validators_add_error_messages	2019-07-03 16:58:21.984844-03
13	auth	0008_alter_user_username_max_length	2019-07-03 16:58:22.006547-03
14	auth	0009_alter_user_last_name_max_length	2019-07-03 16:58:22.02245-03
15	auth	0010_alter_group_name_max_length	2019-07-03 16:58:22.038213-03
16	auth	0011_update_proxy_permissions	2019-07-03 16:58:22.050511-03
17	gestion	0001_initial	2019-07-03 16:58:22.429114-03
18	sessions	0001_initial	2019-07-03 16:58:22.610393-03
19	gestion	0002_auto_20190704_1709	2019-07-04 17:09:46.339816-03
20	gestion	0003_auto_20190705_1600	2019-07-05 16:00:30.73708-03
21	gestion	0004_auto_20190705_1913	2019-07-05 19:13:16.108856-03
22	gestion	0005_auto_20190705_1940	2019-07-05 19:40:45.522156-03
23	gestion	0006_auto_20190718_1239	2019-07-18 12:41:06.971479-03
24	clientes	0001_initial	2019-07-18 12:41:07.011109-03
25	gestion	0007_pedido_cliente	2019-07-18 12:41:07.082474-03
26	clientes	0002_auto_20190719_1211	2019-07-19 12:11:56.86635-03
27	clientes	0002_auto_20190722_1526	2019-07-22 15:26:38.246216-03
28	gestion	0008_auto_20190722_1510	2019-07-22 15:26:55.180255-03
29	productos	0001_initial	2019-07-22 15:26:55.408699-03
30	productos	0002_auto_20190723_1407	2019-07-23 14:07:33.312703-03
31	gestion	0009_delete_proveedor	2019-07-23 14:07:33.324246-03
32	proveedores	0001_initial	2019-07-23 14:07:33.369339-03
33	productos	0003_insumo_proveedores	2019-07-23 14:13:17.251253-03
34	pedidos	0001_initial	2019-07-23 19:41:25.268925-03
35	productos	0004_auto_20190724_2154	2019-07-24 21:55:07.700568-03
36	productos	0005_productimage	2019-07-24 22:51:17.866633-03
37	pedidos	0002_auto_20190731_1154	2019-07-31 11:54:49.952848-03
38	pedidos	0002_auto_20190731_1942	2019-07-31 19:42:28.918229-03
39	productos	0006_auto_20190731_1942	2019-07-31 19:42:28.941855-03
40	productos	0007_producto_slug	2019-07-31 20:43:42.001122-03
41	productos	0008_auto_20190731_2045	2019-07-31 20:45:52.130544-03
42	productos	0009_remove_producto_slug	2019-07-31 20:50:47.827023-03
43	pedidos	0003_productospedido	2019-08-01 11:55:17.174713-03
44	pedidos	0004_remove_pedido_productos_pedido	2019-08-01 13:19:16.717657-03
45	pedidos	0005_pedido_productos_pedido	2019-08-01 13:19:30.10593-03
46	clientes	0003_auto_20190806_1806	2019-08-06 18:06:36.139495-03
47	productos	0010_auto_20190809_1143	2019-08-09 11:43:59.653005-03
48	pedidos	0006_auto_20190809_1743	2019-08-09 17:44:12.677561-03
49	productos	0011_auto_20190809_1743	2019-08-09 17:44:12.692609-03
50	compras	0001_initial	2019-08-27 19:33:10.612077-03
51	compras	0002_insumoscompra_precio_compra	2019-08-27 19:51:40.413138-03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
mh964ff5hraq7jezhi5cx3vb72lyb13w	NzgwZWZjYTY0ZThlNzZmN2E5ZjRjM2ZmYTMzMDFjMzMwMDQ4YmU2Mjp7fQ==	2019-07-24 17:32:08.191603-03
2pl0vit83pu22a3rderkdj0yxvnmuosb	MDk2OTg3MDIwZmY3YTliYjk1NGJiZTUwODczNWUwYTg3MDk1Mzk5Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYjk2ODk4NmViNWRjZGZkNDNiNTYyNjU2OTdiMTM2NmUyMjdmODkzIn0=	2019-07-24 21:38:35.950921-03
rvy0bzgwrbl76nin0c1k3nsqqiv5r5m6	MDk2OTg3MDIwZmY3YTliYjk1NGJiZTUwODczNWUwYTg3MDk1Mzk5Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYjk2ODk4NmViNWRjZGZkNDNiNTYyNjU2OTdiMTM2NmUyMjdmODkzIn0=	2019-07-25 19:16:59.187544-03
lz89roje4jnhw7qcizmhk901q2nv34ur	ZDBhYTcyMmVkNTQ2NDA2NDZjYzk3ODI5NjNjNmZkYTNmOWVmMGRmYjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNTY3MDZmYmFmNzQyODkyODE0ZGFiM2NlNWZjOWU2YjdkZTFkYzQzIn0=	2019-07-25 21:14:06.047965-03
43xx3zb15a9sa38cu6c8njpuff7ln8nr	ZDBhYTcyMmVkNTQ2NDA2NDZjYzk3ODI5NjNjNmZkYTNmOWVmMGRmYjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNTY3MDZmYmFmNzQyODkyODE0ZGFiM2NlNWZjOWU2YjdkZTFkYzQzIn0=	2019-07-26 22:52:22.149429-03
oezttkuc8oe0g9lpne2af1amn0dj8681	ZDBhYTcyMmVkNTQ2NDA2NDZjYzk3ODI5NjNjNmZkYTNmOWVmMGRmYjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNTY3MDZmYmFmNzQyODkyODE0ZGFiM2NlNWZjOWU2YjdkZTFkYzQzIn0=	2019-07-31 19:11:22.7168-03
4jfk9wv8xkn20mrjlfjicc312r53x5bs	ZDBhYTcyMmVkNTQ2NDA2NDZjYzk3ODI5NjNjNmZkYTNmOWVmMGRmYjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNTY3MDZmYmFmNzQyODkyODE0ZGFiM2NlNWZjOWU2YjdkZTFkYzQzIn0=	2019-08-01 13:22:46.343742-03
mh2armvnsxyykq44fvdkcqspavysk6gg	MDk2OTg3MDIwZmY3YTliYjk1NGJiZTUwODczNWUwYTg3MDk1Mzk5Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYjk2ODk4NmViNWRjZGZkNDNiNTYyNjU2OTdiMTM2NmUyMjdmODkzIn0=	2019-08-15 10:33:48.83066-03
t1h4syje9cr7584injd73ndj7xbbpwds	MDk2OTg3MDIwZmY3YTliYjk1NGJiZTUwODczNWUwYTg3MDk1Mzk5Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYjk2ODk4NmViNWRjZGZkNDNiNTYyNjU2OTdiMTM2NmUyMjdmODkzIn0=	2019-08-20 18:01:32.420106-03
iwp5ok2hkcl773lnvyrfkuvot59qt6vn	ZDBhYTcyMmVkNTQ2NDA2NDZjYzk3ODI5NjNjNmZkYTNmOWVmMGRmYjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNTY3MDZmYmFmNzQyODkyODE0ZGFiM2NlNWZjOWU2YjdkZTFkYzQzIn0=	2019-08-26 15:02:07.636495-03
xz61691szlm9rzff07oz7pim6frkkvx6	MDk2OTg3MDIwZmY3YTliYjk1NGJiZTUwODczNWUwYTg3MDk1Mzk5Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYjk2ODk4NmViNWRjZGZkNDNiNTYyNjU2OTdiMTM2NmUyMjdmODkzIn0=	2019-09-03 22:09:36.695362-03
hgu0cfrl4zb7m2unneqcx79y2zcrbu5k	MDk2OTg3MDIwZmY3YTliYjk1NGJiZTUwODczNWUwYTg3MDk1Mzk5Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYjk2ODk4NmViNWRjZGZkNDNiNTYyNjU2OTdiMTM2NmUyMjdmODkzIn0=	2019-09-24 23:02:32.916664-03
\.


--
-- Data for Name: gestion_localidad; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.gestion_localidad (id, localidad, provincia_id, cod_postal) FROM stdin;
1	9 DE JULIO	6	5272
2	ABBURRA	6	5220
3	ACHIRAS	6	5833
4	ACHIRAS	6	5875
5	ACOLLARADO	6	5216
6	ACOSTILLA	6	5871
7	ADELIA MARIA	6	5843
8	AGUA DE CRESPIN	6	5285
9	AGUA DE LAS PIEDRAS	6	5221
10	AGUA DE ORO	6	5107
11	AGUA DE ORO	6	5248
12	AGUA DE TALA	6	5155
13	AGUA DEL TALA	6	5243
14	AGUA HEDIONDA	6	5216
15	AGUA PINTADA	6	5212
16	AGUADA DEL MONTE	6	5209
17	AGUADITA	6	5209
18	AGUAS DE RAMON	6	5284
19	AGUASACHA	6	5221
20	ALCIRA ESTACION GIGENA	6	5813
21	ALEJANDRO ROCA	6	2686
22	ALEJO LEDESMA	6	2662
23	ALGARROBAL	6	5885
24	ALGARROBO	6	5221
25	ALICIA	6	5949
26	ALMAFUERTE	6	5854
27	ALPA CORRAL	6	5801
28	ALPAPUCA	6	5813
29	ALTA GRACIA	6	5186
30	ALTAUTINA	6	5871
31	ALTO ALEGRE	6	5121
32	ALTO ALEGRE	6	5907
33	ALTO CASTRO	6	5182
34	ALTO DE CASTILLO	6	5145
35	ALTO DE FIERRO	6	5119
36	ALTO DE FLORES	6	5203
37	ALTO DE LAS MULAS	6	5875
38	ALTO DE LOS QUEBRACHOS	6	5281
39	ALTO DE SAN PEDRO	6	5174
40	ALTO DEL DURAZNO	6	5119
41	ALTO DEL TALA	6	5295
42	ALTO GRANDE	6	5893
43	ALTO RESBALOSO	6	5885
44	ALTO VERDE	6	5205
45	ALTOS DE CHIPION	6	2417
46	AMBOY	6	5199
47	AMBUL	6	5299
48	ANA ZUMARAN	6	5905
49	ANGOSTURA	6	5155
50	ANIMI	6	5107
51	ANISACATE	6	5189
52	ANTONIO CATALANO	6	6271
53	ARBOL BLANCO	6	5216
54	ARBOL CHATO	6	2432
55	ARBOLES BLANCOS	6	5873
56	ARCOYO	6	5297
57	ARIAS	6	2624
58	AROMITO	6	2341
59	ARROYITO	6	2434
60	ARROYO	6	5297
61	ARROYO ALGODON	6	5909
62	ARROYO CABRAL	6	5917
63	ARROYO DE ALVAREZ	6	2434
64	ARROYO DEL PINO	6	5901
65	ARROYO LA HIGUERA	6	5889
66	ARROYO LOS PATOS	6	5889
67	ARROYO SAN ANTONIO	6	5859
68	ARROYO SANTA CATALINA	6	5825
69	ARROYO SANTANA	6	5819
70	ARROYO SECO	6	5196
71	ARROYO TOLEDO	6	5819
72	ARSENAL JOSE MARIA ROJAS	6	5825
73	ASCOCHINGA	6	5117
74	ASSUNTA	6	2671
75	ATAHONA	6	5225
76	ATHOS PAMPA	6	5194
77	ATUMI PAMPA	6	5196
78	AUGUSTO VANDERSANDE	6	5145
79	AUSONIA	6	5901
80	AVELLANEDA	6	5212
81	BAJADA NUEVA	6	5813
82	BAJO CHICO	6	5189
83	BAJO CHICO BAJO GRANDE	6	5101
84	BAJO DE FERNANDEZ	6	5101
85	BAJO DE GOMEZ	6	5961
86	BAJO DE OLMOS	6	5221
87	BAJO DEL BURRO	6	2662
88	BAJO DEL CARMEN	6	5189
89	BAJO EL MOLINO	6	5887
90	BAJO GALINDEZ	6	5961
91	BAJO GRANDE	6	5101
92	BAJO HONDO	6	5231
93	BAJO LINDO	6	5270
94	BALBUENA	6	5248
95	BALDE DE LA MORA	6	5871
96	BALDE DE LA ORILLA	6	5871
97	BALDE LINDO	6	5871
98	BALLESTEROS	6	2572
99	BALLESTEROS SUD	6	2572
100	BALNEARIA	6	5141
101	BALNEARIO GUGLIERI	6	5137
102	BAÑADO DE PAJA	6	5871
103	BAÑADO DE SOTO	6	5285
104	BAÑADO DEL FUERTE	6	5248
105	BANDA DE VARELA	6	5875
106	BARRANCA YACO	6	5212
107	BARRETO	6	2671
108	BARRETO	6	5246
109	BARRIAL	6	5281
110	BARRIALITOS	6	5284
111	BARRIO BELGRANO	6	2550
112	BARRIO DEAN FUNES	6	5123
113	BARRIO DEL LIBERTADOR	6	5850
114	BARRIO LA FERIA	6	5870
115	BARRIO LA FORTUNA	6	2594
116	BARRIO LOZA	6	5111
117	BARRIO MULLER	6	5143
118	BATAN	6	5155
119	BELEN	6	5220
120	BELL VILLE	6	2550
121	BELLA VISTA	6	5284
122	BENGOLEA	6	5807
123	BENJAMIN GOULD	6	2664
124	BERROTARAN	6	5817
125	BEUCE	6	5244
126	BIALET MASSE	6	5158
127	BLAS DE ROSALES	6	5125
128	BOCA DEL RIO	6	5885
129	BORDO DE LOS ESPINOSA	6	5209
130	BOSQUE ALEGRE	6	5187
131	BOUWER	6	5119
132	BRINKMANN	6	2419
133	BUEN RETIRO	6	5155
134	BUENA VISTA	6	5121
135	BUENA VISTA	6	5249
136	BUENA VISTA	6	5295
137	BUENA VISTA	6	5297
138	BUEY MUERTO	6	5135
139	BULNES	6	5845
140	BURMEISTER	6	6225
141	CABALANGO	6	5155
142	CABANA	6	5109
143	CABEZA DE BUEY	6	5229
144	CABINDO	6	5221
145	CACHI YACO	6	5209
146	CACHIYULLO	6	5284
147	CAJON DEL RIO	6	5184
148	CALABALUMBA	6	5282
149	CALASUYA	6	5201
150	CALCHIN	6	5969
151	CALCHIN OESTE	6	5965
152	CALERA CENTRAL	6	5151
153	CALMAYO	6	5191
154	CAMARONES	6	5205
155	CAMILO ALDAO	6	2585
156	CAMINIAGA	6	5244
157	CAMINO A PUNTA DEL AGUA	6	5101
158	CAMOATI	6	5231
159	CAMPAMENTO MINNETTI	6	5149
160	CAMPO ALEGRE	6	5209
161	CAMPO ALEGRE	6	5221
162	CAMPO ALVAREZ	6	5229
163	CAMPO AMBROGGIO	6	5915
164	CAMPO BANDILLO	6	5943
165	CAMPO BEIRO	6	2421
166	CAMPO BOERO	6	2426
167	CAMPO BOURDICHON	6	5149
168	CAMPO CALVO	6	2423
169	CAMPO COYUNDA	6	5139
170	CAMPO DE LA TORRE	6	5801
171	CAMPO DE LAS PIEDRAS	6	5236
172	CAMPO GENERAL PAZ	6	2555
173	CAMPO GRANDE	6	5231
174	CAMPO LA LUISA	6	2423
175	CAMPO LA PIEDRA	6	5221
176	CAMPO RAMALLO	6	5225
177	CAMPO ROSSIANO	6	5987
178	CAMPO SAN ANTONIO	6	5821
179	CAMPO SAN JUAN	6	6271
180	CAMPO SOL DE MAYO	6	2679
181	CAÑA CRUZ	6	5248
182	CAÑADA ANCHA SANTA ROSA	6	5135
183	CAÑADA DE ALVAREZ	6	5819
184	CAÑADA DE CORIA	6	5249
185	CAÑADA DE CUEVAS	6	5101
186	CAÑADA DE JUME	6	5221
187	CAÑADA DE LAS CHACRAS	6	5199
188	CAÑADA DE LAS GATIADAS	6	5291
189	CAÑADA DE LUQUE	6	5229
190	CAÑADA DE MACHADO	6	5961
191	CAÑADA DE MACHADO SUD	6	5963
192	CAÑADA DE MATEO	6	5221
193	CAÑADA DE MAYO	6	5218
194	CAÑADA DE POCHO	6	5299
195	CAÑADA DE RIO PINTO	6	5221
196	CAÑADA DE SALAS	6	5299
197	CAÑADA DEL DURAZNO	6	5196
198	CAÑADA DEL PUERTO	6	5297
199	CAÑADA DEL SAUCE	6	5817
200	CAÑADA DEL SIMBOL	6	5200
201	CAÑADA DEL TALA	6	5244
202	CAÑADA DEL TALA	6	5859
203	CAÑADA GRANDE	6	5873
204	CAÑADA GRANDE	6	5891
205	CAÑADA HONDA	6	5227
206	CAÑADA HONDA	6	5280
207	CAÑADA LARGA	6	5889
208	CAÑADA SAN ANTONIO	6	5131
209	CAÑADA VERDE	6	6275
210	CAÑADAS HONDAS	6	5221
211	CAÑADON DE LOS MOGOTES	6	5184
212	CANALS	6	2650
213	CANDELARIA	6	5287
214	CANDELARIA SUD	6	5221
215	CANDONGA	6	5111
216	CANTERA LOS VIERAS	6	5212
217	CANTERAS ALTA GRACIA	6	5186
218	CANTERAS EL MANZANO	6	5107
219	CANTERAS EL SAUCE	6	5107
220	CANTERAS IGUAZU	6	5285
221	CANTERAS KILOMETRO 428	6	5200
222	CANTERAS LA CALERA	6	5151
223	CANTERAS LOS MORALES	6	5238
224	CANTERAS QUILPO	6	5281
225	CAP GRAL BERNARDO O HIGGINS	6	2645
226	CAPILLA DE COSME	6	5101
227	CAPILLA DE DOLORES	6	5125
228	CAPILLA DE LOS REMEDIOS	6	5101
229	CAPILLA DE ROMERO	6	5873
230	CAPILLA DE SAN ANTONIO	6	2559
231	CAPILLA DE SITON	6	5231
232	CAPILLA DE TEGUA	6	5813
233	CAPILLA DEL CARMEN	6	5963
234	CAPILLA DEL MONTE	6	5184
235	CAPILLA LA ESPERANZA	6	5129
236	CAPILLA SAN ANTONIO	6	2432
237	CAPILLA SAN ANTONIO DE YUCAT	6	5936
238	CAPILLA SANTA ROSA	6	2415
239	CARAHUASI	6	5196
240	CARLOMAGNO	6	5925
241	CARNERILLO	6	5805
242	CARNERO YACO	6	5246
243	CAROYA	6	5223
244	CARRILOBO	6	5915
245	CARRIZAL	6	5285
246	CARRIZAL	6	5299
247	CARTABEROL	6	5871
248	CASA BAMBA	6	5151
249	CASA BLANCA	6	5299
250	CASA DE PIEDRA	6	5891
251	CASA GRANDE	6	5162
252	CASA NUEVA	6	5155
253	CASA SERRANA HUERTA GRANDE	6	5175
254	CASAS VEJAS	6	5246
255	CASAS VIEJAS	6	5236
256	CASAS VIEJAS	6	5285
257	CASCADAS	6	5178
258	CASPICHUMA	6	5209
259	CASPICUCHANA	6	5209
260	CASSAFFOUSTH ESTACION FCGB	6	5149
261	CASTELLANOS	6	5135
262	CAVANAGH	6	2625
263	CAYUQUEO	6	5901
264	CERRO BLANCO	6	5191
265	CERRO BOLA	6	5293
266	CERRO COLORADO	6	5244
267	CERRO COLORADO	6	5821
268	CERRO DE LA CRUZ	6	5200
269	CERRO NEGRO	6	5221
270	CERRO NEGRO	6	5297
271	CERRO SAN LORENZO	6	5821
272	CERROS ASPEROS	6	5859
273	CHACHA DEL REY	6	5282
274	CHACRAS	6	5284
275	CHACRAS DEL POTRERO	6	5284
276	CHACRAS DEL SAUCE	6	5244
277	CHACRAS VIEJAS	6	5242
278	CHAJAN	6	5837
279	CHALACEA	6	5229
280	CHAMICO	6	5299
281	CHAÑAR VIEJO	6	5246
282	CHAÑARIACO	6	5291
283	CHAÑARITOS	6	5829
284	CHANCANI	6	5871
285	CHAQUINCHUNA	6	5870
286	CHARACATO	6	5287
287	CHARBONIER	6	5282
288	CHARCAS NORTE	6	5127
289	CHARRAS	6	5807
290	CHAZON	6	2675
291	CHILE CORRAL AL AGUADA	6	5246
292	CHILIBROSTE	6	2561
293	CHILLI CORRAL	6	5246
294	CHIPITIN	6	5244
295	CHUA	6	5871
296	CHUCHIRAS	6	5875
297	CHUCUL	6	5805
298	CHUÑA	6	5218
299	CHUÑA HUASI	6	5201
300	CHURQUI CAÑADA	6	5246
301	CIENAGA DE ALLENDE	6	5891
302	CIENAGA DE BRITOS	6	5297
303	CIENAGA DEL CORO	6	5289
304	CINTRA	6	2559
305	CNIA HOGAR VELEZ SARSFIELD	6	5119
306	CNIA VACACIONES DE EMPLEADO	6	5857
307	COLAZO	6	5965
308	COLONIA 10 DE JULIO	6	2349
309	COLONIA 25 LOS SURGENTES	6	2581
310	COLONIA ALEMANA	6	5196
311	COLONIA ALMADA	6	5987
312	COLONIA ANGELITA	6	5941
313	COLONIA ANITA	6	2413
314	COLONIA ARROYO DE ALVAREZ	6	2436
315	COLONIA BALLESTEROS	6	2662
316	COLONIA BANCO PCIA BS AS	6	5155
317	COLONIA BARGE	6	2659
318	COLONIA BEIRO	6	2421
319	COLONIA BISMARCK	6	2651
320	COLONIA BOERO	6	6270
321	COLONIA BOTTURI	6	2419
322	COLONIA BREMEN	6	2651
323	COLONIA CALCHAQUI	6	2580
324	COLONIA CAÑADON	6	5137
325	COLONIA CAROYA	6	5223
326	COLONIA CEFERINA	6	2415
327	COLONIA CORTADERA	6	2436
328	COLONIA COSME SUD	6	5101
329	COLONIA COYUNDA	6	2435
330	COLONIA CRISTINA	6	2424
331	COLONIA DEAN FUNES	6	5847
332	COLONIA DEL BANCO NACION	6	2428
333	COLONIA DOLORES	6	5809
334	COLONIA DOROTEA	6	6270
335	COLONIA DOS HERMANOS	6	2421
336	COLONIA EL CARMEN PARAJE	6	5801
337	COLONIA EL CHAJA	6	2594
338	COLONIA EL FORTIN	6	5133
339	COLONIA EL MILAGRO	6	2424
340	COLONIA EL TRABAJO	6	2424
341	COLONIA EUGENIA	6	2413
342	COLONIA GARZON	6	5987
343	COLONIA GENERAL DEHEZA	6	5945
344	COLONIA GORCHS	6	2415
345	COLONIA HAMBURGO	6	5933
346	COLONIA HOLANDESA	6	5131
347	COLONIA ITALIANA	6	2645
348	COLONIA ITURRASPE	6	2413
349	COLONIA LA ARGENTINA	6	5137
350	COLONIA LA ARGENTINA	6	6140
351	COLONIA LA CALLE	6	5196
352	COLONIA LA CARMENSITA	6	6141
353	COLONIA LA CELESTINA	6	5847
354	COLONIA LA LEONCITA	6	2559
355	COLONIA LA LOLA	6	2650
356	COLONIA LA MAGDALENA DE ORO	6	6132
357	COLONIA LA MOROCHA	6	2423
358	COLONIA LA MURIUCHA	6	2580
359	COLONIA LA PALESTINA	6	2645
360	COLONIA LA PIEDRA	6	5801
361	COLONIA LA PRIMAVERA	6	5933
362	COLONIA LA PROVIDENCIA	6	6134
363	COLONIA LA TORDILLA	6	2435
364	COLONIA LA TRINCHERA	6	2417
365	COLONIA LAS CUATRO ESQUINAS	6	5135
366	COLONIA LAS PICHANAS	6	2433
367	COLONIA LAVARELLO	6	2415
368	COLONIA LEDESMA	6	2662
369	COLONIA LOS VASCOS	6	2189
370	COLONIA LUQUE	6	5850
371	COLONIA MAIPU	6	2684
372	COLONIA MARINA	6	2424
373	COLONIA MASCHI	6	2559
374	COLONIA MAUNIER	6	2349
375	COLONIA MILESSI	6	2349
376	COLONIA MONTES NEGROS	6	5875
377	COLONIA NUEVO PIAMONTE	6	2415
378	COLONIA ORCOVI	6	5841
379	COLONIA PALO LABRADO	6	2415
380	COLONIA PASO CARRIL	6	5801
381	COLONIA PRODAMONTE	6	2413
382	COLONIA PROGRESO	6	2645
383	COLONIA PROSPERIDAD	6	2423
384	COLONIA SAGRADA FAMILIA	6	5125
385	COLONIA SAN BARTOLOME	6	2426
386	COLONIA SAN IGNACIO	6	5189
387	COLONIA SAN ISIDRO	6	5189
388	COLONIA SAN PEDRO	6	2421
389	COLONIA SAN RAFAEL	6	2433
390	COLONIA SANTA ANA	6	6123
391	COLONIA SANTA CATALINA	6	5851
392	COLONIA SANTA MARGARITA	6	5933
393	COLONIA SANTA MARIA	6	2423
394	COLONIA SANTA PAULA	6	5805
395	COLONIA SANTA RITA	6	2411
396	COLONIA SANTA RITA	6	5936
397	COLONIA SILVIO PELLICO	6	5907
398	COLONIA TACURALES	6	2421
399	COLONIA TIROLESA	6	5101
400	COLONIA TORO PUJIO	6	5139
401	COLONIA UDINE	6	2417
402	COLONIA VALLE GRANDE	6	6121
403	COLONIA VALTELINA	6	2413
404	COLONIA VEINTICINCO	6	2592
405	COLONIA VICENTE AGUERO	6	5221
406	COLONIA VIDELA	6	5865
407	COLONIA VIGNAUD	6	2419
408	COLONIA YARETA	6	5137
409	COLONIA YUCAT SUD	6	5917
410	COLONIAS	6	2436
411	COLUMBO	6	5220
412	COME TIERRA	6	5875
413	COMECHINGONES	6	5129
414	COMECHINGONES	6	5153
415	CONCEPCION	6	5871
416	CONDOR HUASI	6	5871
417	CONLARA	6	5873
418	CONSTITUCION	6	5125
419	COPACABANA	6	5201
420	COPINA	6	5153
421	CORDOBA	6	5000
422	CORIMAYO	6	5184
423	CORITO	6	5200
424	CORONEL BAIGORRIA	6	5811
425	CORONEL MOLDES	6	5847
426	CORRAL DE BARRANCA	6	5221
427	CORRAL DE BUSTOS	6	2645
428	CORRAL DE CABALLOS	6	5870
429	CORRAL DE GOMEZ	6	5135
430	CORRAL DE GOMEZ	6	5139
431	CORRAL DE GUARDIA	6	5940
432	CORRAL DE MULAS	6	5945
433	CORRAL DEL BAJO	6	5913
434	CORRAL DEL REY	6	5249
435	CORRAL VIEJO	6	5246
436	CORRALITO	6	5853
437	CORRALITO SAN JAVIER	6	5879
438	CORTADERAS	6	2661
439	COSQUIN	6	5166
440	COSTA ALEGRE	6	5963
441	COSTA DEL CASTAÑO	6	5137
442	COSTA DEL RIO QUINTO	6	6271
443	COSTA DEL TAMBO	6	5801
444	COSTA SACATE	6	5961
445	COTAGAITA	6	2419
446	CRISTINA	6	2424
447	CRUZ ALTA	6	2189
448	CRUZ CHICA	6	5178
449	CRUZ DE CAÑA	6	5287
450	CRUZ DE CAÑA	6	5875
451	CRUZ DEL EJE	6	5280
452	CRUZ DEL QUEMADO	6	5221
453	CRUZ MOJADA	6	5212
454	CUATRO CAMINOS	6	2551
455	CUATRO VIENTOS	6	5801
456	CUCHILLA NEVADA	6	5155
457	CUCHILLO YACO	6	5295
458	CUESTA BLANCA	6	5153
459	CURAPALIGUE	6	6120
460	DALMACIO VELEZ SARSFIELD	6	5919
461	DE LA SERNA	6	6271
462	DEAN FUNES	6	5200
463	DEL CAMPILLO	6	6271
464	DEMARCHI	6	2684
465	DESAGUADERO	6	5284
466	DESPEÑADEROS	6	5121
467	DESVIO CHALACEA	6	5229
468	DESVIO EL VOLCAN	6	5299
469	DESVIO KILOMETRO 57	6	2625
470	DEVOTO	6	2424
471	DIEGO DE ROJAS	6	5135
472	DIEZ RIOS	6	5875
473	DIQUE CHICO	6	5189
474	DIQUE LA VIÑA	6	5885
475	DIQUE LAS VAQUERIAS	6	5168
476	DIQUE LOS MOLINOS	6	5192
477	DIQUE SAN ROQUE	6	5149
478	DOCTOR NICASIO SALAS OROÑO	6	5221
479	DOLORES NUÑEZ DEL PRADO	6	5131
480	DOLORES SAN ESTEBAN	6	5182
481	DOMINGO FUNES	6	5164
482	DOS ARROYOS	6	5189
483	DOS LAGUNAS	6	5813
484	DOS RIOS	6	5155
485	DOS RIOS	6	5297
486	DOS ROSAS	6	2349
487	DUARTE QUIROS	6	5119
488	DUMESNIL	6	5149
489	DURAZNO	6	5244
490	EL AGUILA BLANCA	6	5184
491	EL ALCALDE	6	5131
492	EL ALGADOBAL	6	5885
493	EL ALGARROBAL	6	5249
494	EL ALGARROBO	6	5221
495	EL ALGODONAL	6	5107
496	EL ALTO	6	5885
497	EL ALTO	6	5887
498	EL ARAÑADO	6	5947
499	EL ARBOL	6	6127
500	EL BAGUAL	6	5137
501	EL BAJO	6	5889
502	EL BALDECITO	6	5182
503	EL BALDECITO	6	5870
504	EL BAÑADO	6	5214
505	EL BAÑADO	6	5244
506	EL BAÑADO	6	5248
507	EL BAÑADO	6	5801
508	EL BARREAL	6	5270
509	EL BARREAL	6	5813
510	EL BARRIAL	6	5285
511	EL BORDO	6	5871
512	EL BOSQUE	6	5229
513	EL BRETE	6	5281
514	EL CALLEJON	6	5172
515	EL CANO	6	5821
516	EL CARACOL	6	5284
517	EL CARMEN	6	2550
518	EL CARMEN	6	5197
519	EL CARMEN GUIÑAZU	6	5145
520	EL CARRILITO	6	5963
521	EL CARRIZAL	6	5135
522	EL CARRIZAL	6	5282
523	EL CARRIZAL	6	5299
524	EL CARRIZAL	6	5963
525	EL CARRIZAL CHUÑAHUASI	6	5201
526	EL CERRITO	6	5205
527	EL CERRO	6	5875
528	EL CHACHO	6	5272
529	EL CHANCHITO	6	5218
530	EL CHINGOLO	6	5145
531	EL CHIQUILLAN	6	5813
532	EL CORO	6	5212
533	EL CORO	6	5248
534	EL CORTE	6	5889
535	EL CRESTON DE PIEDRA	6	5236
536	EL CRISPIN	6	5129
537	EL CUADRADO	6	5172
538	EL DESCANSO	6	2434
539	EL DESMONTE	6	5205
540	EL DIQUECITO	6	5151
541	EL DIVISADERO	6	5212
542	EL DORADO	6	2651
543	EL DURAZNITO	6	5801
544	EL DURAZNO	6	5155
545	EL DURAZNO	6	5231
546	EL DURAZNO	6	5249
547	EL DURAZNO	6	5293
548	EL ESPINAL	6	5133
549	EL ESPINILLAL	6	5813
550	EL ESPINILLO	6	5131
551	EL ESTANQUE	6	5212
552	EL FLORENTINO	6	5951
553	EL FLORIDA	6	2432
554	EL FORTIN	6	5951
555	EL FRANCES	6	5282
556	EL FUERTECITO	6	2428
557	EL GABINO	6	5248
558	EL GALLEGO	6	5249
559	EL GATEADO	6	5101
560	EL GUAICO	6	5285
561	EL GUANACO	6	5231
562	EL GUINDO	6	5244
563	EL IALITA	6	5212
564	EL JORDAN	6	5248
565	EL JUME	6	5218
566	EL JUMIAL	6	5947
567	EL LAUREL	6	5248
568	EL MANANTIAL	6	5819
569	EL MANANTIAL	6	5873
570	EL MANGRULLO	6	5249
571	EL MANZANO	6	5107
572	EL MEDANITO	6	5871
573	EL MIRADOR	6	5891
574	EL MOJONCITO	6	5218
575	EL MOLINO	6	5214
576	EL MOLINO	6	5220
577	EL MOYANO	6	5272
578	EL NOY	6	6127
579	EL OCHENTA	6	5123
580	EL OJO DE AGUA	6	5203
581	EL OVERO	6	2563
582	EL PAMPERO	6	6273
583	EL PANAL	6	2580
584	EL PANTANILLO	6	5246
585	EL PANTANILLO	6	5885
586	EL PANTANO	6	5244
587	EL PARADOR DE LA MONTAÑA	6	5197
588	EL PARAISO	6	2559
589	EL PARAISO	6	5218
590	EL PASO	6	5203
591	EL PASO DE LA PAMPA	6	5871
592	EL PASTOR	6	5151
593	EL PAYADOR	6	5151
594	EL PEDACITO	6	5236
595	EL PERCHEL	6	5166
596	EL PERCHEL	6	5244
597	EL PERCHEL	6	5885
598	EL PERTIGO	6	5201
599	EL PERUEL	6	5155
600	EL PILCADO	6	5155
601	EL PINGO	6	5178
602	EL PORTEÑO	6	5933
603	EL PORTEZUELO	6	5196
604	EL PORTILLO	6	5200
605	EL PORVENIR	6	2651
606	EL POTOSI	6	5801
607	EL POTRERO	6	5155
608	EL POTRERO	6	5295
609	EL POZO	6	5233
610	EL PRADO	6	5248
611	EL PROGRESO	6	5249
612	EL PUEBLITO	6	5107
613	EL PUEBLITO	6	5875
614	EL PUENTE	6	5172
615	EL PUESTO	6	5249
616	EL PUESTO	6	5284
617	EL PUESTO LOS CABRERA	6	5218
618	EL QUEBRACHAL	6	5101
619	EL QUEBRACHITO	6	5109
620	EL QUEBRACHO	6	5101
621	EL QUEBRACHO	6	5218
622	EL QUEBRACHO	6	5249
623	EL QUEBRACHO	6	5854
624	EL QUICHO	6	5270
625	EL RANCHITO	6	5218
626	EL RASTREADOR	6	6121
627	EL REYMUNDO	6	5220
628	EL RINCON	6	5231
629	EL RINCON	6	5282
630	EL RINCON	6	5871
631	EL RIO	6	5285
632	EL RODEITO	6	5201
633	EL RODEO	6	5246
634	EL RODEO	6	5249
635	EL RODEO	6	5291
636	EL ROSARIO	6	5205
637	EL SALTO	6	5282
638	EL SALTO NORTE	6	5854
639	EL SAUCE	6	5196
640	EL SAUCE	6	5289
641	EL SAUZAL	6	5887
642	EL SEBIL	6	5244
643	EL SILVERIO	6	5248
644	EL SIMBOL	6	5249
645	EL SIMBOLAR	6	5281
646	EL SUNCHAL	6	5291
647	EL TAJAMAR	6	5885
648	EL TALA	6	5201
649	EL TALAR	6	5107
650	EL TALITA	6	5212
651	EL TALITA VILLA GRAL MITRE	6	5236
652	EL TAMBERO	6	5212
653	EL TAMBO	6	5801
654	EL TIO	6	2432
655	EL TOMILLO	6	5149
656	EL TORREON	6	5864
657	EL TOSTADO	6	5137
658	EL TRABAJO	6	2424
659	EL TRIANGULO	6	2572
660	EL TULE	6	5249
661	EL TUSCAL	6	5216
662	EL VADO	6	5182
663	EL VALLECITO	6	5172
664	EL VALLESITO	6	5291
665	EL VEINTICINCO	6	5214
666	EL VENCE	6	5231
667	EL VERGEL	6	5155
668	EL VISMAL	6	5233
669	EL ZAINO	6	5149
670	EL ZAPALLAR	6	5233
671	EL ZAPATO	6	5184
672	ELENA	6	5815
673	EMBALSE	6	5856
674	ENCRUCIJADA	6	5231
675	ENFERMERA KELLY	6	2587
676	ESCOBAS	6	5282
677	ESCUELA DE ARTILLERIA	6	5101
678	ESPERANZA	6	5131
679	ESPINILLO	6	5129
680	ESPINILLO	6	5203
681	ESPINILLO	6	5221
682	ESPINILLO	6	5811
683	ESPINILLO NUÑEZ DEL PRADO	6	5131
684	ESQUINA	6	5131
685	ESQUINA DEL ALAMBRE	6	5281
686	EST CANDELARIA NORTE	6	5235
687	EST JUAREZ CELMAN	6	5145
688	ESTACION ACHIRAS	6	5831
689	ESTACION BELL VILLE	6	2550
690	ESTACION CALCHIN	6	5969
691	ESTACION CAROYA	6	5220
692	ESTACION COLONIA TIROLESA	6	5131
693	ESTACION GENERAL PAZ	6	5145
694	ESTACION PUNTA DE AGUA	6	5839
695	ESTACION SOTO	6	5284
696	ESTANCIA BOTTARO	6	5229
697	ESTANCIA DE GUADALUPE	6	5291
698	ESTANCIA DOS RIOS	6	5155
699	ESTANCIA EL CARMEN	6	5131
700	ESTANCIA EL CHAÑAR	6	2428
701	ESTANCIA EL NACIONAL	6	5244
702	ESTANCIA EL TACO	6	5229
703	ESTANCIA GOROSITO	6	5212
704	ESTANCIA LA CHIQUITA	6	2428
705	ESTANCIA LA MOROCHA	6	2428
706	ESTANCIA LA PUNTA DEL AGUA	6	5187
707	ESTANCIA LAS CAÑAS	6	5131
708	ESTANCIA LAS MARGARITAS	6	2671
709	ESTANCIA LAS MERCEDES	6	5229
710	ESTANCIA LAS ROSAS	6	5229
711	ESTANCIA LOS MATORRALES	6	5987
712	ESTANCIA PATIÑO	6	5249
713	ESTANCIA VIEJA	6	5152
714	ETRURIA	6	2681
715	EUFRASIO LOZA	6	5248
716	FABRICA MILITAR	6	5189
717	FABRICA MILITAR	6	5900
718	FABRICA MILITAR RIO TERCERO	6	5850
719	FALDA DE CAÑETE	6	5186
720	FALDA DE LOS REARTES	6	5189
721	FALDA DEL CARMEN	6	5187
722	FERREYRA	6	5925
723	FLORA	6	2525
724	FRAGUEYRO	6	5847
725	FRAY CAYETANO RODRIGUEZ	6	6120
726	FREYRE	6	2413
727	GALPON CHICO	6	5967
728	GAVILAN	6	6132
729	GENERAL BALDISSERA	6	2583
730	GENERAL CABRERA	6	5809
731	GENERAL DEHEZA	6	5923
732	GENERAL FOTHERINGHAM	6	5933
733	GENERAL LAS HERAS	6	5101
734	GENERAL LEVALLE	6	6132
735	GENERAL ORTIZ DE OCAMPO	6	5151
736	GENERAL PUEYRREDON	6	6140
737	GENERAL ROCA	6	2592
738	GENERAL SOLER	6	6142
739	GENERAL VIAMONTE	6	2671
740	GLORIALDO FERNANDEZ	6	5837
741	GOLPE DE AGUA	6	5187
742	GRACIELA	6	5209
743	GRUTA DE SAN ANTONIO	6	5172
744	GUALLASCATE	6	5244
745	GUANACO BOLEADO	6	5875
746	GUANACO MUERTO	6	5281
747	GUARDIA VIEJA	6	6120
748	GUASAPAMPA	6	5285
749	GUASTA	6	5155
750	GUATIMOZIN	6	2627
751	GUINDAS	6	5821
752	GUTEMBERG	6	5249
753	HARAS SAN ANTONIO	6	5236
754	HARAS SANTA MARTHA	6	5123
755	HERNANDO	6	5929
756	HIGUERIAS	6	5131
757	HIGUERILLAS	6	5125
758	HIPOLITO BOUCHARD	6	6225
759	HOLMBERG	6	5825
760	HORNILLOS	6	5885
761	HOSPITAL FLIA DOMINGO FUNES	6	5165
762	HUANCHILLA	6	6121
763	HUANCHILLA SUD	6	6121
764	HUASCHA	6	5218
765	HUASTA	6	5875
766	HUCLE	6	5887
767	HUERTA GRANDE	6	5174
768	HUINCA RENANCO	6	6270
769	IDIAZABAL	6	2557
770	IGLESIA VIEJA	6	5270
771	IMPIRA	6	5987
772	INDEPENDENCIA	6	5988
773	INDIA MUERTA	6	5909
774	INGENIERO BERTINI	6	5200
775	INRIVILLE	6	2587
776	INVERNADA	6	5209
777	IRIGOYEN	6	5168
778	ISCHILIN	6	5201
779	ISLA DE SAN ANTONIO	6	5214
780	ISLA DEL CERRO	6	5129
781	ISLA LARGA	6	5129
782	ISLA VERDE	6	2661
783	ISLA VERDE	6	5225
784	ISLA VERDE	6	5893
785	ISLETA NEGRA	6	2559
786	ITALO	6	6271
787	ITI HUASI	6	5203
788	JAIME PETER	6	5218
789	JAMES CRAIK	6	5984
790	JARILLAS	6	5209
791	JEANMAIRE	6	2424
792	JERONIMO CORTES	6	5141
793	JESUS MARIA	6	5220
794	JOSE DE LA QUINTANA	6	5189
795	JOVITA	6	6127
796	JUAN BAUTISTA ALBERDI	6	5891
797	JUAN GARCIA	6	5212
798	JUAREZ CELMAN	6	5145
799	JULIO ARGENTINO ROCA	6	6134
800	JUME	6	5209
801	JUSTINIANO POSSE	6	2553
802	KILEGRUMAN	6	2625
803	KILOMETRO 25	6	5107
804	KILOMETRO 25 LA CARBONADA	6	5123
805	KILOMETRO 267	6	5901
806	KILOMETRO 271	6	5139
807	KILOMETRO 294	6	5137
808	KILOMETRO 316	6	5137
809	KILOMETRO 364	6	5229
810	KILOMETRO 394	6	5238
811	KILOMETRO 430	6	5200
812	KILOMETRO 450	6	5218
813	KILOMETRO 505	6	5280
814	KILOMETRO 531	6	2424
815	KILOMETRO 541	6	5284
816	KILOMETRO 545	6	6142
817	KILOMETRO 55	6	6121
818	KILOMETRO 57	6	2619
819	KILOMETRO 579	6	5168
820	KILOMETRO 581	6	2428
821	KILOMETRO 592	6	5166
822	KILOMETRO 608	6	5149
823	KILOMETRO 658	6	5125
824	KILOMETRO 679	6	5123
825	KILOMETRO 680 RUTA 9	6	5123
826	KILOMETRO 691	6	5125
827	KILOMETRO 692	6	5123
828	KILOMETRO 711	6	5125
829	KILOMETRO 730	6	5145
830	KILOMETRO 745	6	5220
831	KILOMETRO 784	6	5212
832	KILOMETRO 807	6	5212
833	KILOMETRO 827	6	5212
834	KILOMETRO 832	6	5200
835	KILOMETRO 859	6	5214
836	KILOMETRO 865	6	5214
837	KILOMETRO 881	6	5214
838	KILOMETRO 907	6	5216
839	KILOMETRO 931	6	5216
840	LA ABRA	6	5281
841	LA AGUADA	6	5211
842	LA AGUADA	6	5212
843	LA AGUADA	6	5285
844	LA AGUADA	6	5801
845	LA AGUADITA	6	5299
846	LA AGUADITA	6	5887
847	LA ARGENTINA	6	5293
848	LA AURA	6	5218
849	LA BANDA	6	5249
850	LA BARRANCA	6	5214
851	LA BARRANCA	6	5248
852	LA BARRANQUITA	6	5833
853	LA BATALLA	6	5201
854	LA BATEA	6	5270
855	LA BETANIA	6	5189
856	LA BISMUTINA	6	5291
857	LA BOTIJA	6	5214
858	LA BRIANZA	6	5848
859	LA BUENA PARADA	6	5129
860	LA CAJUELA	6	2563
861	LA CALERA	6	5151
862	LA CALERA	6	5218
863	LA CALERA	6	5297
864	LA CALERA	6	5813
865	LA CALERA	6	5819
866	LA CAÑADA	6	5101
867	LA CAÑADA	6	5155
868	LA CAÑADA	6	5231
869	LA CAÑADA	6	5870
870	LA CAÑADA ANGOSTA	6	5218
871	LA CAÑADA GRANDE	6	5803
872	LA CAÑADA SANTA CRUZ	6	5201
873	LA CANTERA	6	5168
874	LA CARBONERA	6	5280
875	LA CARLOTA	6	2670
876	LA CAROLINA	6	5841
877	LA CASCADA	6	5854
878	LA CAUTIVA	6	6142
879	LA CELINA	6	5125
880	LA CESIRA	6	6101
881	LA CHACRA	6	5212
882	LA CHICHARRA	6	5249
883	LA CHOZA	6	5196
884	LA CIENAGA	6	5133
885	LA COCHA	6	5101
886	LA COCHA	6	5893
887	LA COLONIA	6	5201
888	LA COLORADA	6	5831
889	LA COMPASION	6	5871
890	LA CONCEPCION	6	5281
891	LA CONCEPCION	6	5870
892	LA CORTADERA	6	2434
893	LA CORTADERA	6	5871
894	LA COSTA	6	5244
895	LA COSTA	6	5249
896	LA COSTA	6	5282
897	LA COSTA	6	5885
898	LA COTITA	6	5220
899	LA CRUZ	6	5249
900	LA CRUZ	6	5859
901	LA CUMBRE	6	5178
902	LA CUMBRE	6	5801
903	LA CUMBRECITA	6	5194
904	LA CURVA	6	2434
905	LA DORA	6	5229
906	LA DORMIDA	6	5817
907	LA ESPERANZA	6	5209
908	LA ESPERANZA	6	5231
909	LA ESQUINA	6	5295
910	LA ESQUINA	6	5801
911	LA ESTACADA	6	5212
912	LA ESTANCIA	6	5249
913	LA ESTANCIA	6	5291
914	LA ESTANCITA	6	5111
915	LA ESTRELLA	6	5129
916	LA FALDA	6	5172
917	LA FLORIDA	6	5214
918	LA FLORIDA	6	5281
919	LA FRANCIA	6	2426
920	LA FRONDA	6	5282
921	LA FRONTERA	6	2433
922	LA FUENTE	6	5879
923	LA GILDA	6	5848
924	LA GRAMILLA	6	5282
925	LA GRANADILLA	6	5187
926	LA GRANJA	6	5115
927	LA GRUTA	6	5889
928	LA GUARDIA	6	5891
929	LA HERRADURA	6	5900
930	LA HIGUERA	6	5285
931	LA HIGUERITA	6	5201
932	LA HIGUERITA	6	5244
933	LA INVERNADA	6	5801
934	LA ISABELA	6	5200
935	LA ISLA	6	5186
936	LA ISLETA	6	5963
937	LA ISOLINA	6	5186
938	LA ITALIANA	6	2651
939	LA JARILLA	6	5871
940	LA LAGUNA	6	5205
941	LA LAGUNA	6	5284
942	LA LAGUNA	6	5901
943	LA LAGUNILLA	6	5119
944	LA LAGUNILLA	6	5825
945	LA LILIA	6	5281
946	LA LINEA	6	5871
947	LA LUZ	6	6271
948	LA MAJADA	6	5212
949	LA MAJADA	6	5887
950	LA MAZA	6	5231
951	LA MERCANTIL	6	5841
952	LA MESADA	6	5200
953	LA MESADA	6	5801
954	LA MESILLA	6	5285
955	LA MILKA	6	2400
956	LA MOSTAZA	6	5137
957	LA MUDANA	6	5299
958	LA NACIONAL	6	6275
959	LA OSCURIDAD	6	5255
960	LA PAISANITA	6	5186
961	LA PALESTINA	6	5925
962	LA PALMA	6	5231
963	LA PALMERINA	6	5913
964	LA PAMPA	6	5117
965	LA PAQUITA	6	2417
966	LA PARA	6	5137
967	LA PATRIA	6	5871
968	LA PAZ	6	5117
969	LA PAZ	6	5879
970	LA PENCA	6	5231
971	LA PENCA	6	6279
972	LA PERLITA	6	6271
973	LA PIEDRA BLANCA	6	5246
974	LA PIEDRA MOVEDIZA	6	5184
975	LA PINTADA	6	5248
976	LA PINTADA	6	5271
977	LA PLAYA	6	5285
978	LA PLAYOSA	6	5911
979	LA PLAZA	6	5244
980	LA POBLACION	6	5875
981	LA POBLADORA	6	5945
982	LA PORFIA	6	5119
983	LA PORTEÑA	6	5221
984	LA POSTA	6	5227
985	LA POSTA CHUÑAGUAS	6	5201
986	LA PRIMAVERA	6	5139
987	LA PROVIDENCIA	6	5231
988	LA PUERTA	6	5101
989	LA PUERTA	6	5137
990	LA PUERTA	6	5281
991	LA PUERTA VILLA DE SOTO	6	5284
992	LA QUEBRADA	6	5107
993	LA QUEBRADA	6	5172
994	LA QUEBRADA	6	5297
995	LA QUINTA	6	5135
996	LA QUINTA	6	5209
997	LA QUINTA	6	5887
998	LA QUINTANA	6	5249
999	LA RAMADA	6	5875
1000	LA RAMADA	6	6123
1001	LA RAMONCITA	6	5813
1002	LA REDENCION	6	5105
1003	LA REDUCCION	6	2594
1004	LA REDUCCION	6	5105
1005	LA REINA	6	5925
1006	LA REPRESA	6	2436
1007	LA RINCONADA	6	5233
1008	LA RINCONADA CANDELARIA	6	5249
1009	LA ROSARINA	6	5951
1010	LA RUDA	6	5214
1011	LA SELVA	6	5212
1012	LA SERRANITA	6	5189
1013	LA SIENA	6	5875
1014	LA SIERRITA	6	5297
1015	LA SIERRITA	6	5813
1016	LA SOLEDAD	6	5249
1017	LA TABLADA	6	5299
1018	LA TIGRA	6	5949
1019	LA TOMA	6	5244
1020	LA TOMA	6	5280
1021	LA TOMA	6	5889
1022	LA TOTORILLA	6	5209
1023	LA TRAMPA	6	5871
1024	LA TRAVESIA	6	5875
1025	LA TRINCHERA	6	2417
1026	LA TUNA	6	5212
1027	LA TUNA TINOCO	6	5131
1028	LA UDINE	6	2413
1029	LA USINA	6	5168
1030	LA VENTANA	6	5870
1031	LA VERONICA	6	5801
1032	LA VICENTA	6	2417
1033	LA VICTORIA	6	5231
1034	LA VIRGINIA	6	5220
1035	LA VIRGINIA	6	5281
1036	LA ZANJA	6	5201
1037	LA ZARA	6	5913
1038	LA ZARITA	6	5913
1039	LABORDE	6	2657
1040	LABOULAYE	6	6120
1041	LADERA YACUS	6	5246
1042	LAGUNA BRAVA	6	5244
1043	LAGUNA CLARA	6	5813
1044	LAGUNA DE GOMEZ	6	5244
1045	LAGUNA LARGA	6	5974
1046	LAGUNA LARGA SUD	6	5988
1047	LAGUNA OSCURA	6	6144
1048	LAGUNA SECA	6	5829
1049	LAGUNILLA	6	5101
1050	LAGUNILLA	6	5972
1051	LAGUNILLAS	6	5807
1052	LARSEN	6	6275
1053	LAS ABAHACAS	6	5801
1054	LAS ABRAS	6	5270
1055	LAS ACACIAS	6	5129
1056	LAS ACEQUIAS	6	5848
1057	LAS AGUADITAS	6	5201
1058	LAS ALBAHACAS	6	5801
1059	LAS ALERAS	6	5270
1060	LAS AROMAS	6	5231
1061	LAS ARRIAS	6	5231
1062	LAS ASTILLAS	6	5220
1063	LAS AVERIAS	6	5135
1064	LAS BAJADAS	6	5851
1065	LAS BANDURRIAS	6	5236
1066	LAS BANDURRIAS NORTE	6	5225
1067	LAS CABRAS	6	5127
1068	LAS CALECITAS	6	5801
1069	LAS CALERAS	6	5819
1070	LAS CALLES	6	5885
1071	LAS CAÑADAS	6	5284
1072	LAS CAÑADAS	6	5870
1073	LAS CAÑAS	6	5101
1074	LAS CAÑAS	6	5201
1075	LAS CAÑAS	6	5216
1076	LAS CAÑAS	6	5246
1077	LAS CAÑITAS	6	2428
1078	LAS CAÑITAS	6	5801
1079	LAS CANTERAS	6	5218
1080	LAS CARDAS	6	5248
1081	LAS CASITAS	6	5158
1082	LAS CEBOLLAS	6	5885
1083	LAS CHACRAS	6	5214
1084	LAS CHACRAS	6	5249
1085	LAS CHACRAS	6	5284
1086	LAS CHACRAS	6	5297
1087	LAS CHACRAS	6	5875
1088	LAS CHACRAS RUTA 111 KM 14	6	5101
1089	LAS CINCO CUADRAS	6	5841
1090	LAS CONANITAS	6	5885
1091	LAS CORTADERAS	6	5249
1092	LAS CORTADERAS	6	5293
1093	LAS CORTADERAS	6	5295
1094	LAS CRUCECITAS	6	5201
1095	LAS CUATRO ESQUINAS	6	5900
1096	LAS CUSENADAS	6	5109
1097	LAS DELICIAS	6	2433
1098	LAS DELICIAS	6	5212
1099	LAS ENCADENADAS	6	5109
1100	LAS ENCRUCIJADAS	6	5871
1101	LAS ENSENADAS	6	5153
1102	LAS ENSENADAS	6	5825
1103	LAS FLORES	6	5249
1104	LAS GAMAS	6	5819
1105	LAS GEMELAS	6	5184
1106	LAS GRAMILLAS	6	5135
1107	LAS GRAMILLAS	6	5246
1108	LAS GUINDAS	6	5801
1109	LAS HERAS	6	5101
1110	LAS HIGUERAS	6	5805
1111	LAS HIGUERILLAS	6	5131
1112	LAS HIGUERITAS	6	5186
1113	LAS HIGUERITAS	6	5199
1114	LAS HILERAS	6	5137
1115	LAS HORQUETAS	6	5244
1116	LAS ISLETILLAS	6	5931
1117	LAS JARILLAS	6	5209
1118	LAS JARILLAS	6	5871
1119	LAS JUNTAS	6	5203
1120	LAS JUNTURAS	6	5965
1121	LAS LAGUNITAS	6	2568
1122	LAS LATAS	6	5272
1123	LAS LOMAS	6	5284
1124	LAS LOMITAS	6	5212
1125	LAS LOMITAS	6	5244
1126	LAS MANZANAS	6	5212
1127	LAS MASITAS	6	5231
1128	LAS MERCEDES	6	5249
1129	LAS MERCEDITAS	6	2572
1130	LAS MOJARRAS	6	5909
1131	LAS MORAS	6	5801
1132	LAS OSCURAS	6	5871
1133	LAS OVERIAS	6	2559
1134	LAS PALMAS	6	5201
1135	LAS PALMAS	6	5231
1136	LAS PALMAS	6	5299
1137	LAS PALMERAS	6	2559
1138	LAS PALMITAS	6	5221
1139	LAS PALMITAS	6	5227
1140	LAS PALMITAS	6	5889
1141	LAS PALOMAS	6	5870
1142	LAS PALOMITAS	6	5201
1143	LAS PAMPILLAS	6	5182
1144	LAS PEÑAS	6	5238
1145	LAS PEÑAS	6	5817
1146	LAS PEÑAS NORTE	6	5823
1147	LAS PEÑAS SUD	6	5819
1148	LAS PENCAS	6	5200
1149	LAS PERDICES	6	5921
1150	LAS PICHANAS	6	5900
1151	LAS PIEDRAS ANCHAS	6	5212
1152	LAS PIEDRITAS	6	5281
1153	LAS PIGUAS	6	5129
1154	LAS PLAYAS	6	5172
1155	LAS PLAYAS	6	5285
1156	LAS PLAYAS LOZADA	6	5101
1157	LAS QUINTAS	6	5244
1158	LAS RABONAS	6	5885
1159	LAS ROSAS	6	5295
1160	LAS SALADAS	6	5137
1161	LAS SIERRAS	6	5212
1162	LAS SIERRITAS	6	5199
1163	LAS TAPIAS	6	5281
1164	LAS TAPIAS	6	5801
1165	LAS TAPIAS	6	5885
1166	LAS TINAJERAS	6	5284
1167	LAS TOSCAS	6	5214
1168	LAS TOSCAS	6	5871
1169	LAS TOTORITAS	6	5285
1170	LAS TRANCAS	6	5246
1171	LAS TRES PIEDRAS	6	5879
1172	LAS TUSCAS	6	5218
1173	LAS VAQUERIAS	6	5184
1174	LAS VARAS	6	5941
1175	LAS VARILLAS	6	5940
1176	LAS VERTIENTES	6	5839
1177	LAS VERTIENTES DE LA GRANJA	6	5107
1178	LATAN HALL	6	2625
1179	LECUEDER	6	6273
1180	LEGUIZAMON	6	6128
1181	LEONES	6	2594
1182	LO MACHADO	6	5246
1183	LOBERA	6	5201
1184	LOMA BLANCA	6	5209
1185	LOMA BOLA	6	5879
1186	LOMA DE PIEDRA	6	5244
1187	LOMA REDONDA	6	5299
1188	LOMAS DEL TROZO	6	5137
1189	LOMITAS	6	5209
1190	LOMITAS	6	5875
1191	LOS ALAMOS	6	5244
1192	LOS ALFALFARES	6	6275
1193	LOS ALGARROBITOS	6	2432
1194	LOS ALGARROBITOS	6	5225
1195	LOS ALGARROBITOS	6	5281
1196	LOS ALGARROBOS	6	5189
1197	LOS ALGARROBOS	6	5887
1198	LOS ALVAREZ	6	5133
1199	LOS AVILES	6	5137
1200	LOS BARRIALES	6	5291
1201	LOS BORDOS	6	5209
1202	LOS BRINZES	6	5201
1203	LOS CADILLOS	6	5214
1204	LOS CAJONES	6	5246
1205	LOS CALLEJONES	6	5220
1206	LOS CALLEJONES	6	5871
1207	LOS CASTAÑOS	6	5137
1208	LOS CEDROS	6	5101
1209	LOS CEJAS	6	5201
1210	LOS CERRILLOS	6	5101
1211	LOS CERRILLOS	6	5209
1212	LOS CERRILLOS	6	5246
1213	LOS CERRILLOS	6	5871
1214	LOS CERROS	6	5137
1215	LOS CERROS NEGROS	6	5821
1216	LOS CHAÑARES	6	5133
1217	LOS CHAÑARES	6	5212
1218	LOS CHAÑARES	6	5220
1219	LOS CHAÑARES	6	5873
1220	LOS CHAÑARITOS	6	5125
1221	LOS CHAÑARITOS	6	5281
1222	LOS CHAÑARITOS	6	5873
1223	LOS CIGARRALES	6	5107
1224	LOS CISNES	6	2684
1225	LOS COCOS	6	5182
1226	LOS COCOS	6	5246
1227	LOS COCOS	6	5821
1228	LOS COMETIERRA	6	5221
1229	LOS CONDORES	6	5823
1230	LOS COQUITOS	6	5201
1231	LOS DESAGUES	6	2421
1232	LOS DOS POZOS	6	5871
1233	LOS DOS RIOS	6	5220
1234	LOS DURAZNOS	6	5220
1235	LOS ESLABONES	6	5270
1236	LOS GAUCHOS DE GUEMES	6	6127
1237	LOS GIGANTES	6	5155
1238	LOS GUEVARA	6	5282
1239	LOS GUINDOS	6	5127
1240	LOS HELECHOS	6	5168
1241	LOS HORMIGUEROS	6	5281
1242	LOS HORNILLOS	6	5885
1243	LOS HOYOS	6	5249
1244	LOS HUESOS	6	5153
1245	LOS JAGUELES	6	5839
1246	LOS JUSTES	6	5249
1247	LOS MANGUITOS	6	5873
1248	LOS MANSILLAS	6	5127
1249	LOS MEDANITOS	6	5871
1250	LOS MEDANOS	6	5815
1251	LOS MIGUELITOS	6	5137
1252	LOS MIQUILES	6	5221
1253	LOS MISTOLES	6	5229
1254	LOS MISTOLES	6	5281
1255	LOS MOGOTES	6	5182
1256	LOS MOLINOS	6	5189
1257	LOS MOLLES	6	2561
1258	LOS MOLLES	6	5885
1259	LOS MOLLES	6	5887
1260	LOS MORTEROS	6	5214
1261	LOS OLIVARES	6	5101
1262	LOS PANTALLES	6	5284
1263	LOS PANTANILLOS	6	5125
1264	LOS PARAISOS	6	5187
1265	LOS PAREDONES	6	5282
1266	LOS PEDERNALES	6	5212
1267	LOS PIQUILLINES	6	5201
1268	LOS POCITOS	6	5145
1269	LOS POCITOS	6	5249
1270	LOS POTREROS	6	5850
1271	LOS POZOS	6	5212
1272	LOS POZOS	6	5225
1273	LOS POZOS	6	5244
1274	LOS POZOS	6	5249
1275	LOS POZOS	6	5870
1276	LOS PUENTES	6	5158
1277	LOS PUESTITOS	6	5200
1278	LOS QUEBRACHITOS	6	5221
1279	LOS QUEBRACHOS	6	5246
1280	LOS REARTES	6	5194
1281	LOS REYUNOS	6	5925
1282	LOS RUICES	6	5201
1283	LOS SAUCES	6	5282
1284	LOS SOCABONES	6	5214
1285	LOS SURGENTES	6	2581
1286	LOS TAJAMARES	6	5233
1287	LOS TALARES	6	5299
1288	LOS TARTAGOS	6	5218
1289	LOS TASIS	6	2559
1290	LOS TERRONES	6	5184
1291	LOS TRES POZOS	6	5851
1292	LOS TRONCOS	6	5246
1293	LOS UCLES	6	2559
1294	LOS VALDES	6	5270
1295	LOS VAZQUEZ	6	5125
1296	LOS ZORROS	6	5901
1297	LOZADA	6	5101
1298	LUCA	6	5917
1299	LUCIO V MANSILLA	6	5216
1300	LUIS SAUZE	6	2423
1301	LUQUE	6	5967
1302	LUTTI	6	5859
1303	LUXARDO	6	2411
1304	LUYABA	6	5875
1305	MACHA	6	5211
1306	MAJADA DE SANTIAGO	6	5287
1307	MAJADILLA	6	5203
1308	MAJADILLA	6	5209
1309	MALAGUEÑO	6	5101
1310	MALENA	6	5839
1311	MALLIN	6	5155
1312	MALVINAS ARGENTINAS	6	5125
1313	MANANTIALES	6	2671
1314	MANANTIALES	6	5209
1315	MANDALA	6	5284
1316	MANFREDI	6	5988
1317	MANGUITAS	6	5873
1318	MAQUINISTA GALLINI	6	5227
1319	MAR AZUL	6	5199
1320	MARCOS JUAREZ	6	2580
1321	MARIA	6	5925
1322	MARULL	6	5139
1323	MATACOS	6	2659
1324	MATORRALES	6	5965
1325	MATTALDI	6	6271
1326	MAUNIER	6	2421
1327	MAYU SUMAJ	6	5153
1328	MEDIA LUNA	6	5125
1329	MEDIA NARANJA	6	5281
1330	MELIDEO	6	6270
1331	MELO	6	6123
1332	MENDIOLAZA	6	5107
1333	MESA DE MARIANO	6	5285
1334	MESILLAS	6	5153
1335	MI GRANJA	6	5125
1336	MI VALLE	6	5101
1337	MIGUEL SALAS	6	6128
1338	MIGUELITO	6	5225
1339	MINA ARAUJO	6	5297
1340	MINA CLAVERO	6	5889
1341	MINA LA BISMUTINA	6	5291
1342	MIQUILOS	6	5221
1343	MIRAFLORES	6	5244
1344	MIRAFLORES	6	5272
1345	MIRAMAR	6	5143
1346	MODESTINO PIZARRO	6	6273
1347	MODESTO ACUÑA	6	5823
1348	MOGIGASTA	6	5891
1349	MOGOTE VERDE	6	5291
1350	MOLINARI	6	5166
1351	MOLINOS	6	5212
1352	MONSALVO	6	5851
1353	MONTE BUEY	6	2589
1354	MONTE CASTILLO	6	2563
1355	MONTE CRISTO	6	5125
1356	MONTE DE LOS GAUCHOS	6	5831
1357	MONTE DE LOS LAZOS	6	5900
1358	MONTE DE TORO PUJIO	6	5135
1359	MONTE DEL FRAYLE	6	5931
1360	MONTE DEL ROSARIO	6	5129
1361	MONTE GRANDE	6	2417
1362	MONTE GRANDE RAFAEL GARCIA	6	5119
1363	MONTE LA INVERNADA	6	5801
1364	MONTE LEÑA	6	2564
1365	MONTE MAIZ	6	2659
1366	MONTE RALO	6	5119
1367	MONTE REDONDO	6	2423
1368	MONTE REDONDO	6	5889
1369	MONTE REDONDO	6	5963
1370	MORRISON	6	2568
1371	MORTEROS	6	2421
1372	MOVADO	6	5209
1373	MULA MUERTA	6	5221
1374	MUSSI	6	5299
1375	NAVARRO	6	5209
1376	NAZCA	6	6270
1377	NEGRO HUASI	6	5280
1378	NICHO	6	5870
1379	NICOLAS BRUZONE	6	6271
1380	NIDO DEL AGUILA	6	5889
1381	NIÑA PAULA	6	5889
1382	NINALQUIN	6	5291
1383	NINTES	6	5220
1384	NOETINGER	6	2563
1385	NONO	6	5887
1386	ÑU PORA	6	5111
1387	NUEVA ANDALUCIA	6	5101
1388	NUEVA ESPERANZA	6	5280
1389	NUÑEZ DEL PRADO	6	5131
1390	OBISPO TREJO	6	5225
1391	OBREGON	6	5189
1392	OJO DE AGUA	6	5220
1393	OJO DE AGUA	6	5293
1394	OJO DE AGUA	6	5887
1395	OJO DE AGUA DE TOTOX	6	5293
1396	OLAETA	6	5807
1397	OLIVA	6	5980
1398	OLIVARES SAN NICOLAS	6	5280
1399	OLMOS	6	2684
1400	ONAGOITY	6	6227
1401	ONCATIVO	6	5986
1402	ONGAMIRA	6	5184
1403	ORATORIO DE PERALTA	6	5125
1404	ORCOSUNI	6	5214
1405	ORDOÑEZ	6	2555
1406	ORO GRUESO	6	5287
1407	OVERA NEGRA	6	5951
1408	PACHANGO	6	5893
1409	PACHECO DE MELO	6	6121
1410	PAJAS BLANCAS	6	5111
1411	PAJONAL	6	5291
1412	PALO CORTADO	6	5280
1413	PALO LABRADO	6	5281
1414	PALO NEGRO	6	5961
1415	PALO PARADO	6	5281
1416	PALO QUEMADO	6	5284
1417	PALOMA POZO	6	5284
1418	PAMPA DE ACHALA	6	5153
1419	PAMPA DE OLAEN	6	5166
1420	PAMPAYASTA NORTE	6	5931
1421	PAMPAYASTA SUR	6	5931
1422	PANAHOLMA	6	5893
1423	PARQUE SIQUIMAN	6	5158
1424	PASCANAS	6	2679
1425	PASCO	6	5925
1426	PASO CABRAL	6	5817
1427	PASO CASTELLANOS	6	5145
1428	PASO DE LOS GALLEGOS	6	2433
1429	PASO DE MONTOYA	6	5284
1430	PASO DE VELEZ	6	5972
1431	PASO DEL DURAZNO	6	5803
1432	PASO DEL SAUCE	6	5101
1433	PASO DEL SILVERIO	6	5246
1434	PASO GRANDE	6	5291
1435	PASO LAS TROPAS	6	5887
1436	PASO SANDIALITO	6	5819
1437	PASO VIEJO	6	5284
1438	PASTOS ALTOS	6	5807
1439	PAUNERO	6	5738
1440	PAVIN	6	6121
1441	PEDANIA CANDELARIA SUD	6	5233
1442	PEDRO E FUNES	6	2671
1443	PEDRO E VIVAS	6	5127
1444	PERMANENTES	6	5801
1445	PERMANENTES	6	5821
1446	PICHANAS	6	5284
1447	PIEDRA BLANCA	6	5285
1448	PIEDRA BLANCA	6	5801
1449	PIEDRA BLANCA	6	5887
1450	PIEDRA GRANDE	6	5168
1451	PIEDRA MOVEDIZA	6	5174
1452	PIEDRA PINTADA	6	5871
1453	PIEDRAS AMONTONADAS	6	5284
1454	PIEDRAS ANCHAS	6	2645
1455	PIEDRAS ANCHAS	6	5284
1456	PIEDRAS ANCHAS	6	5291
1457	PIEDRAS BLANCAS	6	5174
1458	PIEDRAS GRANDES	6	5172
1459	PIEDRITA BLANCA	6	5271
1460	PIEDRITAS ROSADAS	6	5295
1461	PILAR	6	5972
1462	PINAS	6	2572
1463	PINCEN	6	6271
1464	PIQUILLIN	6	5125
1465	PISCO HUASI	6	5244
1466	PITOA	6	5295
1467	PLAYA GRANDE	6	5139
1468	PLAZA BRUNO	6	2436
1469	PLAZA DE MERCEDES	6	5137
1470	PLAZA MINETTI	6	5967
1471	PLAZA RODRIGUEZ	6	5987
1472	PLAZA SAN FRANCISCO	6	2401
1473	PLUJUNTA	6	5141
1474	POCHO	6	5299
1475	POCITO DEL CAMPO	6	5248
1476	PORTEÑA	6	2415
1477	POTRERO DE FUNES	6	5189
1478	POTRERO DE GARAY	6	5189
1479	POTRERO DE LUJAN	6	5191
1480	POTRERO DE MARQUES	6	5297
1481	POTRERO DE TUTZER	6	5186
1482	POZO CONCA	6	5221
1483	POZO CORREA	6	5221
1484	POZO DE JUANCHO	6	5246
1485	POZO DE LA ESQUINA	6	5133
1486	POZO DE LA LOMA	6	5125
1487	POZO DE LA PAMPA	6	5871
1488	POZO DE LAS OLLAS	6	5249
1489	POZO DE LAS YEGUAS	6	5125
1490	POZO DE LOS ARBOLES	6	5249
1491	POZO DE LOS TRONCOS	6	5137
1492	POZO DE MOLINA	6	5249
1493	POZO DEL AVESTRUZ	6	5947
1494	POZO DEL BARRIAL	6	5272
1495	POZO DEL CHAJA	6	2433
1496	POZO DEL CHAÑAR	6	2435
1497	POZO DEL CHAÑAR	6	5873
1498	POZO DEL MOLLE	6	5873
1499	POZO DEL MOLLE	6	5913
1500	POZO DEL MORO	6	5225
1501	POZO DEL SIMBOL	6	5249
1502	POZO DEL SIMBOL	6	5281
1503	POZO DEL TIGRE	6	5145
1504	POZO DEL TIGRE	6	5209
1505	POZO LA PIEDRA	6	5135
1506	POZO NUEVO	6	5209
1507	POZO SECO	6	5285
1508	POZO SOLO	6	5244
1509	PRETOT FREYRE	6	6140
1510	PRIMAVERA	6	5139
1511	PROVIDENCIA	6	5231
1512	PUEBLO ALBERDI	6	5800
1513	PUEBLO ARGENTINO	6	2580
1514	PUEBLO CARLOS SAUVERAN	6	2581
1515	PUEBLO GAMBANDE	6	2627
1516	PUEBLO ITALIANO	6	2651
1517	PUEBLO PIANELLI	6	5131
1518	PUEBLO RIO TERCERO	6	2581
1519	PUEBLO VIEJO	6	2555
1520	PUENTE DEL CURA	6	5891
1521	PUENTE LOS MOLLES	6	5809
1522	PUENTE RIO PLUJUNTA	6	5139
1523	PUERTA COLORADA	6	5817
1524	PUERTA DE LA QUEBRADA	6	5297
1525	PUESTO DE AFUERA	6	5131
1526	PUESTO DE ARRIBA	6	5214
1527	PUESTO DE BATALLA	6	5218
1528	PUESTO DE CASTRO	6	5233
1529	PUESTO DE CERRO	6	5200
1530	PUESTO DE FIERRO	6	5227
1531	PUESTO DE LA OVEJA	6	5131
1532	PUESTO DE LOS ALAMOS	6	5249
1533	PUESTO DE LOS RODRIGUEZ	6	5200
1534	PUESTO DE LUNA	6	5233
1535	PUESTO DE PUCHETA	6	5225
1536	PUESTO DE VERA	6	5271
1537	PUESTO DEL GALLO	6	5281
1538	PUESTO DEL MEDIO	6	5117
1539	PUESTO DEL ROSARIO	6	5236
1540	PUESTO EL ABRA	6	5284
1541	PUESTO GUZMAN	6	5153
1542	PUESTO MULITA	6	5189
1543	PUESTO NUEVO	6	5209
1544	PUESTO SAN JOSE	6	5242
1545	PUESTO VIEJO	6	5244
1546	PUNILLA	6	5184
1547	PUNTA DEL AGUA	6	5129
1548	PUNTA DEL AGUA	6	5839
1549	PUNTA DEL AGUA	6	5931
1550	PUNTA DEL MONTE	6	5249
1551	PUSISUNA	6	5299
1552	QUEBRACHITOS	6	2436
1553	QUEBRACHO HERRADO	6	2423
1554	QUEBRACHO LADEADO	6	5875
1555	QUEBRACHO SOLO	6	5871
1556	QUEBRACHOS	6	5131
1557	QUEBRADA DE LOS POZOS	6	5885
1558	QUEBRADA DE LUNA	6	5282
1559	QUEBRADA DE NONA	6	5184
1560	QUEBRADA DEL HORNO	6	5889
1561	QUILINO	6	5214
1562	QUILMES	6	5270
1563	QUISCASACATE	6	5221
1564	RACEDO	6	5249
1565	RAFAEL GARCIA	6	5119
1566	RAMALLO	6	5225
1567	RAMBLON	6	5284
1568	RAMIREZ	6	5289
1569	RAMON J CARCANO	6	5900
1570	RANGEL	6	5131
1571	RANQUELES	6	6271
1572	RARA FORTUNA	6	5287
1573	RAYO CORTADO	6	5246
1574	RECREO VICTORIA	6	5144
1575	REDUCCION	6	5803
1576	REPRESA DE MORALES	6	5285
1577	RINCON	6	5961
1578	RINCON CASA GRANDE	6	5162
1579	RINCON DE LUNA	6	5197
1580	RIO ARRIBA	6	5887
1581	RIO BAMBA	6	6134
1582	RIO CEBALLOS	6	5111
1583	RIO CHICO	6	5221
1584	RIO CUARTO	6	5800
1585	RIO DE JAIME	6	5875
1586	RIO DE LA POBLACION	6	5280
1587	RIO DE LAS MANZANAS	6	5212
1588	RIO DE LOS SAUCES	6	5221
1589	RIO DE LOS SAUCES	6	5821
1590	RIO DE LOS TALAS	6	5221
1591	RIO DEL DURAZNO	6	5197
1592	RIO DULCE	6	5249
1593	RIO GRANDE	6	5172
1594	RIO GRANDE AMBOY	6	5199
1595	RIO HONDO	6	5297
1596	RIO HONDO	6	5875
1597	RIO HONDO	6	5891
1598	RIO LOS MOLINOS	6	5189
1599	RIO PEDRO	6	5246
1600	RIO PINTO	6	5221
1601	RIO PRIMERO	6	5127
1602	RIO SAN MIGUEL	6	5249
1603	RIO SECO	6	5284
1604	RIO SECO	6	5801
1605	RIO SEGUNDO	6	5960
1606	RIO TERCERO	6	5850
1607	RIO VIEJO	6	5249
1608	RODEITO	6	5209
1609	RODEO DE LOS CABALLOS	6	5821
1610	RODEO DE PIEDRA	6	5875
1611	RODEO LAS YEGUAS	6	5821
1612	RODEO VIEJO	6	5801
1613	ROJAS	6	5246
1614	ROSALES	6	6128
1615	RUIZ DIAZ DE GUZMAN	6	6120
1616	RUMIACO	6	5289
1617	RUMIHUASI	6	5285
1618	RUTA 111 KILOMETRO 14	6	5101
1619	RUTA 19 KILOMETRO 317	6	5125
1620	SACANTA	6	5945
1621	SAGRADA FAMILIA	6	5297
1622	SAGRADA FAMILIA	6	5875
1623	SAIRA	6	2525
1624	SAJON	6	5200
1625	SALADILLO	6	2587
1626	SALDAN	6	5149
1627	SALGUERO	6	6120
1628	SALSACATE	6	5295
1629	SALSIPUEDES	6	5113
1630	SALTO	6	5873
1631	SAMPACHO	6	5829
1632	SAN AGUSTIN	6	5191
1633	SAN AMBROSIO	6	5848
1634	SAN ANTONIO	6	5121
1635	SAN ANTONIO	6	5281
1636	SAN ANTONIO	6	5870
1637	SAN ANTONIO DE ARREDONDO	6	5153
1638	SAN ANTONIO DE BELLA VISTA	6	5236
1639	SAN ANTONIO DE LITIN	6	2559
1640	SAN ANTONIO DE YUCAT	6	5936
1641	SAN ANTONIO NORTE	6	5119
1642	SAN BARTOLO	6	5249
1643	SAN BARTOLOME	6	5801
1644	SAN BASILIO	6	5841
1645	SAN BERNARDO	6	5201
1646	SAN BERNARDO	6	5848
1647	SAN BUENAVENTURA	6	5164
1648	SAN CARLOS	6	2572
1649	SAN CARLOS	6	5212
1650	SAN CARLOS	6	5291
1651	SAN CLEMENTE	6	5187
1652	SAN CRISTOBAL	6	5107
1653	SAN ESTEBAN	6	5182
1654	SAN EUSEBIO	6	2561
1655	SAN FRANCISCO	6	2400
1656	SAN FRANCISCO DEL CHAÑAR	6	5209
1657	SAN GABRIEL	6	5244
1658	SAN GERONIMO	6	5297
1659	SAN IGNACIO	6	5182
1660	SAN IGNACIO	6	5199
1661	SAN IGNACIO	6	5248
1662	SAN ISIDRO	6	5220
1663	SAN ISIDRO	6	5281
1664	SAN ISIDRO	6	5875
1665	SAN JAVIER	6	5875
1666	SAN JERONIMO	6	5297
1667	SAN JERONIMO	6	5963
1668	SAN JOAQUIN	6	6123
1669	SAN JORGE	6	5117
1670	SAN JOSE	6	2563
1671	SAN JOSE	6	5166
1672	SAN JOSE	6	5216
1673	SAN JOSE	6	5242
1674	SAN JOSE	6	5281
1675	SAN JOSE	6	5871
1676	SAN JOSE	6	5961
1677	SAN JOSE DE LA DORMIDA	6	5244
1678	SAN JOSE DE LAS SALINAS	6	5216
1679	SAN JOSE DEL SALTEÑO	6	2563
1680	SAN JUANCITO	6	5249
1681	SAN LORENZO	6	5221
1682	SAN LORENZO	6	5893
1683	SAN LUCAS NORTE	6	5837
1684	SAN LUIS	6	5209
1685	SAN MARCOS SIERRAS	6	5282
1686	SAN MARCOS SUD	6	2566
1687	SAN MARTIN	6	5249
1688	SAN MELITON	6	2664
1689	SAN MIGUEL	6	5117
1690	SAN MIGUEL	6	5212
1691	SAN MIGUEL SAN VICENTE	6	5871
1692	SAN NICOLAS	6	5187
1693	SAN NICOLAS	6	5281
1694	SAN NICOLAS	6	5871
1695	SAN PABLO	6	5209
1696	SAN PABLO	6	5220
1697	SAN PEDRO	6	2559
1698	SAN PEDRO	6	5249
1699	SAN PEDRO	6	5871
1700	SAN PEDRO DE SAN ALBERTO	6	5871
1701	SAN PEDRO DE TOYOS	6	5201
1702	SAN PEDRO NORTE	6	5205
1703	SAN PELLEGRINO	6	5221
1704	SAN RAFAEL	6	5139
1705	SAN RAFAEL	6	5871
1706	SAN RAFAEL	6	5960
1707	SAN RAMON	6	5137
1708	SAN RAMON	6	5249
1709	SAN ROQUE	6	5149
1710	SAN ROQUE	6	5199
1711	SAN ROQUE	6	5227
1712	SAN ROQUE	6	5870
1713	SAN ROQUE LAS ARRIAS	6	5231
1714	SAN SALVADOR	6	5227
1715	SAN SALVADOR	6	5282
1716	SAN SEBASTIAN	6	5889
1717	SAN VICENTE	6	2550
1718	SAN VICENTE	6	5200
1719	SAN VICENTE	6	5871
1720	SANABRIA	6	5901
1721	SANTA ANA	6	5209
1722	SANTA ANA	6	5284
1723	SANTA CATALINA	6	5221
1724	SANTA CATALINA	6	5248
1725	SANTA CATALINA	6	5825
1726	SANTA CECILIA	6	2561
1727	SANTA CLARA	6	6123
1728	SANTA CRISTINA	6	6134
1729	SANTA CRUZ	6	5201
1730	SANTA ELENA	6	5131
1731	SANTA ELENA	6	5246
1732	SANTA EUFEMIA	6	2671
1733	SANTA ISABEL	6	5249
1734	SANTA ISABEL	6	5282
1735	SANTA LUCIA	6	5229
1736	SANTA MAGDALENA	6	6127
1737	SANTA MARIA	6	2651
1738	SANTA MARIA	6	5236
1739	SANTA MARIA	6	5889
1740	SANTA MARIA DE PUNILLA	6	5164
1741	SANTA MARIA DE SOBREMONTE	6	5209
1742	SANTA MONICA	6	5197
1743	SANTA RITA	6	2413
1744	SANTA RITA	6	5189
1745	SANTA RITA	6	5200
1746	SANTA RITA	6	5893
1747	SANTA ROSA	6	5166
1748	SANTA ROSA	6	5909
1749	SANTA ROSA	6	5913
1750	SANTA ROSA DE CALAMUCHITA	6	5196
1751	SANTA ROSA DE RIO PRIMERO	6	5133
1752	SANTA ROSA HUERTA GRANDE	6	5174
1753	SANTA SABINA	6	5221
1754	SANTA TERESA	6	5221
1755	SANTA VICTORIA	6	2675
1756	SANTANILLA	6	5248
1757	SANTIAGO TEMPLE	6	5125
1758	SANTO DOMINGO	6	5209
1759	SANTO DOMINGO	6	5871
1760	SANTO TOMAS	6	5220
1761	SAPANSOTO	6	5291
1762	SARLACO	6	5196
1763	SARMICA	6	5925
1764	SARMIENTO	6	5212
1765	SATURNINO M LASPIUR	6	5943
1766	SAUCE ARRIBA	6	5182
1767	SAUCE ARRIBA	6	5871
1768	SAUCE CHIQUITO	6	5200
1769	SAUCE DE LOS QUEVEDOS	6	5297
1770	SAUCE PUNCO	6	5200
1771	SEBASTIAN ELCANO	6	5231
1772	SEEBER	6	2419
1773	SEGUNDA USINA	6	5857
1774	SENDAS GRANDES	6	5284
1775	SERRANO	6	6125
1776	SERREZUELA	6	5270
1777	SEVILLA	6	5205
1778	SIERRA BLANCA	6	5819
1779	SIERRA DE ABREGU	6	5291
1780	SIERRA DE LAS PAREDES	6	5291
1781	SIERRAS MORENAS	6	5189
1782	SIMBOLAR	6	5242
1783	SIMBOLAR	6	5281
1784	SINSACATE	6	5220
1785	SOCONCHO	6	5191
1786	SOCORRO	6	5209
1787	SOLAR LOS MOLINOS	6	5189
1788	SOLARES DE YCHO CRUZ	6	5153
1789	SOLEDAD	6	5137
1790	SORIA	6	5829
1791	SUCO	6	5837
1792	SUNCHAL	6	5291
1793	SUNCHO HUICO	6	5184
1794	TABANILLO	6	5870
1795	TABAQUILLO	6	5281
1796	TACO POZO	6	5249
1797	TACUREL	6	6123
1798	TAJAMARES	6	5233
1799	TALA CAÑADA	6	5297
1800	TALA CRUZ	6	5859
1801	TALA DEL RIO SECO	6	5284
1802	TALA HUASI	6	5153
1803	TALA NORTE	6	5131
1804	TALA SUD	6	5127
1805	TALAINI	6	5291
1806	TANCACHA	6	5933
1807	TANTI	6	5155
1808	TANTI LOMAS	6	5155
1809	TANTI NUEVO	6	5155
1810	TARUCA PAMPA	6	5299
1811	TASACUNA	6	5284
1812	TASMA	6	5893
1813	TEGUA	6	5813
1814	TEJEDA	6	5125
1815	TERCER CUERPO DEL EJERCITO	6	5101
1816	TERCERA	6	5189
1817	TICINO	6	5927
1818	TIGRE MUERTO	6	5859
1819	TILQUICHO	6	5873
1820	TIMON CRUZ	6	5129
1821	TINOCO	6	5131
1822	TINTIZACO	6	5229
1823	TIO PUJIO	6	5936
1824	TODOS LOS SANTOS	6	5201
1825	TOLEDO	6	5123
1826	TOMAS ECHENIQUE	6	6271
1827	TORDILLA NORTE	6	2435
1828	TORDILLA NORTE	6	5135
1829	TORO MUERTO	6	5200
1830	TORO MUERTO	6	5295
1831	TORO PUJIO	6	5139
1832	TOSNO	6	5289
1833	TOSQUITA	6	6141
1834	TOTORA GUASI	6	5284
1835	TOTORAL	6	5229
1836	TOTORALEJOS	6	5216
1837	TOTORITAS	6	5291
1838	TOTRILLA	6	5201
1839	TRANSITO	6	2436
1840	TRES ARBOLES	6	5285
1841	TRES CHAÑARES	6	5295
1842	TRES ESQUINAS	6	5291
1843	TRES LOMAS	6	5291
1844	TRES POZOS	6	5972
1845	TRINCHERA	6	5909
1846	TRISTAN NARVAJA	6	5149
1847	TRONCO POZO	6	5223
1848	TUCLAME	6	5284
1849	TULUMBA	6	5203
1850	TUSCAL	6	5216
1851	UCACHA	6	2677
1852	UNIDAD TURISTICA EMBALSE	6	5857
1853	UNQUILLO	6	5109
1854	URITORCO	6	5184
1855	USINA NUCLEAR EMBALSE	6	5859
1856	VACAS BLANCAS	6	5143
1857	VALLE DEL SOL	6	5107
1858	VALLE DORADO	6	5864
1859	VALLE HERMOSO	6	5168
1860	VALLE VERDE	6	5115
1861	VANGUARDIA	6	5246
1862	VIAMONTE	6	2671
1863	VICUÑA MACKENNA	6	6140
1864	VILLA AGUADA DE LOS REYES	6	5857
1865	VILLA AHORA	6	5166
1866	VILLA ALBERTINA	6	5221
1867	VILLA ALLENDE	6	5105
1868	VILLA ALPINA	6	5194
1869	VILLA AMANCAY	6	5199
1870	VILLA ANGELICA	6	5885
1871	VILLA ANISACATE	6	5189
1872	VILLA ASCASUBI	6	5935
1873	VILLA AURORA	6	5900
1874	VILLA BERNA	6	5194
1875	VILLA BUSTOS	6	5164
1876	VILLA CAEIRO	6	5164
1877	VILLA CANDELARIA NORTE	6	5249
1878	VILLA CARLOS PAZ	6	5152
1879	VILLA CARLOS PELLEGRINI	6	5186
1880	VILLA CERRO AZUL	6	5107
1881	VILLA CERRO NEGRO	6	5221
1882	VILLA CIUDAD DE AMERICA	6	5189
1883	VILLA CIUDAD PQUE LOS REARTES	6	5189
1884	VILLA CLODOMIRA	6	5885
1885	VILLA COLIMBA	6	5201
1886	VILLA CONCEPCION DEL TIO	6	2433
1887	VILLA CORAZON DE MARIA	6	5101
1888	VILLA COSTA AZUL	6	5153
1889	VILLA CUESTA BLANCA	6	5153
1890	VILLA CURA BROCHERO	6	5891
1891	VILLA DE LAS ROSAS	6	5885
1892	VILLA DE MARIA	6	5248
1893	VILLA DE SOTO	6	5284
1894	VILLA DEL DIQUE	6	5862
1895	VILLA DEL LAGO	6	5152
1896	VILLA DEL PARQUE	6	5864
1897	VILLA DEL PARQUE	6	5903
1898	VILLA DEL PRADO	6	5186
1899	VILLA DEL ROSARIO	6	5963
1900	VILLA DEL TALA	6	5859
1901	VILLA DEL TOTORAL	6	5236
1902	VILLA DIAZ	6	5109
1903	VILLA DOLORES	6	5870
1904	VILLA EL CHACAY	6	5801
1905	VILLA EL CORCOVADO	6	5199
1906	VILLA EL DESCANSO	6	5189
1907	VILLA EL TORREON	6	5199
1908	VILLA ELISA	6	2594
1909	VILLA EMILIA	6	5900
1910	VILLA ESQUIU	6	5101
1911	VILLA FLOR SERRANA	6	5155
1912	VILLA FONTANA	6	5137
1913	VILLA GENERAL BELGRANO	6	5194
1914	VILLA GENERAL MITRE	6	5236
1915	VILLA GIARDINO	6	5176
1916	VILLA GRACIA	6	5153
1917	VILLA GUTIERREZ	6	5212
1918	VILLA HUIDOBRO	6	6275
1919	VILLA INDEPENDENCIA	6	5153
1920	VILLA LA BOLSA	6	5189
1921	VILLA LA COBA	6	5819
1922	VILLA LA RANCHERITA	6	5189
1923	VILLA LAGO AZUL	6	5199
1924	VILLA LAS MERCEDES	6	5107
1925	VILLA LEONOR	6	5109
1926	VILLA LOS ALTOS	6	5111
1927	VILLA LOS AROMOS	6	5186
1928	VILLA LOS LEONES	6	5281
1929	VILLA LOS PATOS	6	2551
1930	VILLA MAR CHIQUITA	6	5137
1931	VILLA MARIA	6	5220
1932	VILLA MARIA	6	5900
1933	VILLA MIREA	6	5123
1934	VILLA MODERNA	6	6275
1935	VILLA NATURALEZA	6	5864
1936	VILLA NUEVA	6	5903
1937	VILLA PARQUE SANTA ANA	6	5101
1938	VILLA PARQUE SIQUIMAN	6	5152
1939	VILLA POSSE	6	5123
1940	VILLA QUILINO	6	5214
1941	VILLA QUILLINZO	6	5859
1942	VILLA RAFAEL BENEGAS	6	5885
1943	VILLA RIO ICHO CRUZ	6	5153
1944	VILLA ROSARIO DEL SALADILLO	6	5233
1945	VILLA ROSSI	6	6128
1946	VILLA RUMIPAL	6	5864
1947	VILLA SAN ESTEBAN	6	5947
1948	VILLA SAN JAVIER	6	5199
1949	VILLA SAN MIGUEL	6	5111
1950	VILLA SANTA CRUZ DEL LAGO	6	5152
1951	VILLA SANTA MARIA	6	5186
1952	VILLA SANTA RITA	6	5801
1953	VILLA SANTA ROSA	6	5133
1954	VILLA SARMIENTO	6	5871
1955	VILLA SARMIENTO	6	6273
1956	VILLA SATYTA	6	5189
1957	VILLA SIERRAS DEL LAGO	6	5857
1958	VILLA SUIZA ARGENTINA	6	5156
1959	VILLA TANINGA	6	5295
1960	VILLA TORTOSA	6	5109
1961	VILLA VALERIA	6	6273
1962	VILLA VAUDAGNA	6	2435
1963	VILLA VIEJA	6	2426
1964	VILLA YACANTO	6	5197
1965	VISO	6	5295
1966	VISTA ALEGRE	6	5197
1967	VIVERO	6	6128
1968	WASHINGTON	6	6144
1969	WATT	6	6270
1970	WENCESLAO ESCALANTE	6	2655
1971	YACANTO	6	5877
1972	YANACATO	6	5248
1973	YATAY	6	5841
1974	YCHO CRUZ SIERRAS	6	5153
1975	YERBA BUENA	6	5200
1976	YOCSINA	6	5101
1977	ZAPATA	6	5873
1978	ZAPOLOCO	6	5839
\.


--
-- Data for Name: gestion_provincia; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.gestion_provincia (id, cod_provincia, provincia) FROM stdin;
1	AR-B	 Buenos Aires
2	AR-C	 Capital Federal
3	AR-K	 Catamarca
4	AR-H	 Chaco
5	AR-U	 Chubut
6	AR-X	 Córdoba
7	AR-W	 Corrientes
8	AR-E	 Entre Ríos
9	AR-P	 Formosa
10	AR-Y	 Jujuy
11	AR-L	 La Pampa
12	AR-F	 La Rioja
13	AR-M	 Mendoza
14	AR-N	 Misiones
15	AR-Q	 Neuquén
16	AR-R	 Río Negro
17	AR-A	 Salta
18	AR-J	 San Juan
19	AR-D	 San Luis
20	AR-Z	 Santa Cruz
21	AR-S	 Santa Fe
22	AR-G	 Santiago del Estero
23	AR-V	 Tierra del Fuego
24	AR-T	 Tucumán
\.


--
-- Data for Name: pedidos_pedido; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.pedidos_pedido (id, precio_final, detalles, estado, actualizado, fecha_pedido, cliente_id) FROM stdin;
1	650.00		creado	2019-07-23 19:48:39.618924-03	2019-07-23	1
2	455.99		pagado	2019-07-24 12:32:38.046101-03	2019-07-24	1
3	455.99		pagado	2019-07-24 12:40:02.760818-03	2019-07-24	1
4	455.99		pagado	2019-07-24 12:40:27.409667-03	2019-07-24	1
5	850.00	Entregado en tiempo y forma.	entregado	2019-08-01 19:23:33.995947-03	2019-08-01	1
6	456.00	prueba	pagado	2019-08-02 12:19:08.599403-03	2019-08-02	2
7	456.00	prueba	pagado	2019-08-02 12:20:42.699014-03	2019-08-02	2
8	123.00	Prueba admin	pagado	2019-08-02 19:22:54.967669-03	2019-08-02	2
9	998.98	prueba	pagado	2019-08-05 12:14:08.763914-03	2019-08-05	2
10	122.96	prueba	entregado	2019-08-27 18:48:37.520185-03	2019-08-05	2
11	456.00		pagado	2019-08-27 18:48:57.179419-03	2019-08-05	1
\.


--
-- Data for Name: pedidos_productospedido; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.pedidos_productospedido (id, cantidad, pedido_id, producto_id) FROM stdin;
1	3	5	10
2	2	5	11
4	1	7	10
5	4	8	10
6	3	8	11
7	2	9	10
8	2	9	11
9	1	9	10
10	5	10	10
11	4	10	11
12	50	11	10
\.


--
-- Data for Name: productos_caracteristica; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.productos_caracteristica (id, nombre, detalles) FROM stdin;
2	Largo	Medida en cm del largo del producto
3	Ancho	
4	Alto	
\.


--
-- Data for Name: productos_caracteristicasproducto; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.productos_caracteristicasproducto (id, valor, caracteristica_id, producto_id) FROM stdin;
2	30	2	10
3	25	3	10
4	4	4	10
5	50	2	13
6	40	3	13
7	4	4	13
\.


--
-- Data for Name: productos_insumo; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.productos_insumo (id, nombre, descripcion, medida, precio, unidad_medida_id) FROM stdin;
1	MDF-3	Plancha de fibrofacil de 3mm de grosor.	380*280	75.00	1
2	Lija-80	Lija 80 porosidad	1	15.00	2
3	Cola Vinílica		4.5	450.00	3
4	MDF-5	FF 5mm	380*280	300.00	1
\.


--
-- Data for Name: productos_insumo_proveedores; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.productos_insumo_proveedores (id, insumo_id, proveedor_id) FROM stdin;
1	2	1
2	3	1
3	4	2
\.


--
-- Data for Name: productos_insumosproducto; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.productos_insumosproducto (id, cantidad, insumo_id, producto_id) FROM stdin;
25	5	1	10
26	1	2	10
27	2	3	10
28	5	1	11
29	3	2	11
30	2	3	11
31	4	1	12
32	2	2	12
33	1	3	12
\.


--
-- Data for Name: productos_productimage; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.productos_productimage (id, imagen, producto_id) FROM stdin;
\.


--
-- Data for Name: productos_producto; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.productos_producto (id, nombre, descripcion, precio) FROM stdin;
10	Bandeja 30*25*4	Bandeja de fibrofacil	150
11	Bastidor 35*25	Bastidor de fibrofacil	200
12	Reloj 30*30		100
13	Bandeja 50*40*4	Esta bandeja es más grande	500
\.


--
-- Data for Name: productos_stockinsumo; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.productos_stockinsumo (id, cantidad, detalles, insumo_id) FROM stdin;
\.


--
-- Data for Name: productos_unidad; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.productos_unidad (id, nombre, descripcion) FROM stdin;
1	cm	Centímetro
2	U	Unidad
3	Kg	Kilogramo
\.


--
-- Data for Name: proveedores_proveedor; Type: TABLE DATA; Schema: public; Owner: enredarteadmin
--

COPY public.proveedores_proveedor (id, cuit, razon_social, telefono, email, calle, numero, detalles, localidad_id) FROM stdin;
1	30-59895662-2	VIA PUBLICA CLAN S.A.	123456789	empresa@proveedor.com	Sarmiento	789		1931
2	27-34290818-2	NEGRETE S.A.	3534123456	empresa@proveedor.com	San Martin	1894	NEGRO	1931
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 128, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 3, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: compras_compra_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.compras_compra_id_seq', 1, false);


--
-- Name: compras_insumoscompra_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.compras_insumoscompra_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 76, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 32, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 51, true);


--
-- Name: gestion_cliente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.gestion_cliente_id_seq', 2, true);


--
-- Name: gestion_localidad_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.gestion_localidad_id_seq', 1978, true);


--
-- Name: gestion_provincia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.gestion_provincia_id_seq', 24, true);


--
-- Name: pedidos_pedido_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.pedidos_pedido_id_seq', 12, true);


--
-- Name: pedidos_productospedido_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.pedidos_productospedido_id_seq', 14, true);


--
-- Name: productos_caracteristica_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.productos_caracteristica_id_seq', 4, true);


--
-- Name: productos_caracteristicasproducto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.productos_caracteristicasproducto_id_seq', 7, true);


--
-- Name: productos_insumo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.productos_insumo_id_seq', 4, true);


--
-- Name: productos_insumo_proveedores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.productos_insumo_proveedores_id_seq', 3, true);


--
-- Name: productos_insumosproducto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.productos_insumosproducto_id_seq', 33, true);


--
-- Name: productos_productimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.productos_productimage_id_seq', 5, true);


--
-- Name: productos_producto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.productos_producto_id_seq', 13, true);


--
-- Name: productos_stockinsumo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.productos_stockinsumo_id_seq', 1, false);


--
-- Name: productos_unidad_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.productos_unidad_id_seq', 3, true);


--
-- Name: proveedores_proveedor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: enredarteadmin
--

SELECT pg_catalog.setval('public.proveedores_proveedor_id_seq', 2, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: compras_compra compras_compra_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.compras_compra
    ADD CONSTRAINT compras_compra_pkey PRIMARY KEY (id);


--
-- Name: compras_insumoscompra compras_insumoscompra_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.compras_insumoscompra
    ADD CONSTRAINT compras_insumoscompra_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: clientes_cliente gestion_cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.clientes_cliente
    ADD CONSTRAINT gestion_cliente_pkey PRIMARY KEY (id);


--
-- Name: gestion_localidad gestion_localidad_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.gestion_localidad
    ADD CONSTRAINT gestion_localidad_pkey PRIMARY KEY (id);


--
-- Name: gestion_provincia gestion_provincia_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.gestion_provincia
    ADD CONSTRAINT gestion_provincia_pkey PRIMARY KEY (id);


--
-- Name: pedidos_pedido pedidos_pedido_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.pedidos_pedido
    ADD CONSTRAINT pedidos_pedido_pkey PRIMARY KEY (id);


--
-- Name: pedidos_productospedido pedidos_productospedido_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.pedidos_productospedido
    ADD CONSTRAINT pedidos_productospedido_pkey PRIMARY KEY (id);


--
-- Name: productos_caracteristica productos_caracteristica_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_caracteristica
    ADD CONSTRAINT productos_caracteristica_pkey PRIMARY KEY (id);


--
-- Name: productos_caracteristicasproducto productos_caracteristicasproducto_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_caracteristicasproducto
    ADD CONSTRAINT productos_caracteristicasproducto_pkey PRIMARY KEY (id);


--
-- Name: productos_insumo productos_insumo_nombre_key; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumo
    ADD CONSTRAINT productos_insumo_nombre_key UNIQUE (nombre);


--
-- Name: productos_insumo productos_insumo_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumo
    ADD CONSTRAINT productos_insumo_pkey PRIMARY KEY (id);


--
-- Name: productos_insumo_proveedores productos_insumo_proveed_insumo_id_proveedor_id_98d6fced_uniq; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumo_proveedores
    ADD CONSTRAINT productos_insumo_proveed_insumo_id_proveedor_id_98d6fced_uniq UNIQUE (insumo_id, proveedor_id);


--
-- Name: productos_insumo_proveedores productos_insumo_proveedores_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumo_proveedores
    ADD CONSTRAINT productos_insumo_proveedores_pkey PRIMARY KEY (id);


--
-- Name: productos_insumosproducto productos_insumosproducto_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumosproducto
    ADD CONSTRAINT productos_insumosproducto_pkey PRIMARY KEY (id);


--
-- Name: productos_productimage productos_productimage_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_productimage
    ADD CONSTRAINT productos_productimage_pkey PRIMARY KEY (id);


--
-- Name: productos_producto productos_producto_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_producto
    ADD CONSTRAINT productos_producto_pkey PRIMARY KEY (id);


--
-- Name: productos_stockinsumo productos_stockinsumo_insumo_id_key; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_stockinsumo
    ADD CONSTRAINT productos_stockinsumo_insumo_id_key UNIQUE (insumo_id);


--
-- Name: productos_stockinsumo productos_stockinsumo_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_stockinsumo
    ADD CONSTRAINT productos_stockinsumo_pkey PRIMARY KEY (id);


--
-- Name: productos_unidad productos_unidad_nombre_key; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_unidad
    ADD CONSTRAINT productos_unidad_nombre_key UNIQUE (nombre);


--
-- Name: productos_unidad productos_unidad_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_unidad
    ADD CONSTRAINT productos_unidad_pkey PRIMARY KEY (id);


--
-- Name: proveedores_proveedor proveedores_proveedor_cuit_key; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.proveedores_proveedor
    ADD CONSTRAINT proveedores_proveedor_cuit_key UNIQUE (cuit);


--
-- Name: proveedores_proveedor proveedores_proveedor_pkey; Type: CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.proveedores_proveedor
    ADD CONSTRAINT proveedores_proveedor_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: compras_compra_proveedor_id_d647dfa3; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX compras_compra_proveedor_id_d647dfa3 ON public.compras_compra USING btree (proveedor_id);


--
-- Name: compras_insumoscompra_compra_id_1a5038d1; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX compras_insumoscompra_compra_id_1a5038d1 ON public.compras_insumoscompra USING btree (compra_id);


--
-- Name: compras_insumoscompra_insumo_id_29202c98; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX compras_insumoscompra_insumo_id_29202c98 ON public.compras_insumoscompra USING btree (insumo_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: gestion_cliente_localidad_id_0a7e274d; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX gestion_cliente_localidad_id_0a7e274d ON public.clientes_cliente USING btree (localidad_id);


--
-- Name: gestion_localidad_provincia_id_4b057c4d; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX gestion_localidad_provincia_id_4b057c4d ON public.gestion_localidad USING btree (provincia_id);


--
-- Name: pedidos_pedido_cliente_id_84f4fc73; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX pedidos_pedido_cliente_id_84f4fc73 ON public.pedidos_pedido USING btree (cliente_id);


--
-- Name: pedidos_productospedido_pedido_id_281119d2; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX pedidos_productospedido_pedido_id_281119d2 ON public.pedidos_productospedido USING btree (pedido_id);


--
-- Name: pedidos_productospedido_producto_id_24373755; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX pedidos_productospedido_producto_id_24373755 ON public.pedidos_productospedido USING btree (producto_id);


--
-- Name: productos_caracteristicasproducto_caracteristica_id_673102d7; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX productos_caracteristicasproducto_caracteristica_id_673102d7 ON public.productos_caracteristicasproducto USING btree (caracteristica_id);


--
-- Name: productos_caracteristicasproducto_producto_id_de124b3b; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX productos_caracteristicasproducto_producto_id_de124b3b ON public.productos_caracteristicasproducto USING btree (producto_id);


--
-- Name: productos_insumo_nombre_3be7af83_like; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX productos_insumo_nombre_3be7af83_like ON public.productos_insumo USING btree (nombre varchar_pattern_ops);


--
-- Name: productos_insumo_proveedores_insumo_id_914827de; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX productos_insumo_proveedores_insumo_id_914827de ON public.productos_insumo_proveedores USING btree (insumo_id);


--
-- Name: productos_insumo_proveedores_proveedor_id_b74124a9; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX productos_insumo_proveedores_proveedor_id_b74124a9 ON public.productos_insumo_proveedores USING btree (proveedor_id);


--
-- Name: productos_insumo_unidad_medida_id_39ad036e; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX productos_insumo_unidad_medida_id_39ad036e ON public.productos_insumo USING btree (unidad_medida_id);


--
-- Name: productos_insumosproducto_insumo_id_711ec9bd; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX productos_insumosproducto_insumo_id_711ec9bd ON public.productos_insumosproducto USING btree (insumo_id);


--
-- Name: productos_insumosproducto_producto_id_ce42865b; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX productos_insumosproducto_producto_id_ce42865b ON public.productos_insumosproducto USING btree (producto_id);


--
-- Name: productos_productimage_producto_id_30689d5d; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX productos_productimage_producto_id_30689d5d ON public.productos_productimage USING btree (producto_id);


--
-- Name: productos_unidad_nombre_6bcf3768_like; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX productos_unidad_nombre_6bcf3768_like ON public.productos_unidad USING btree (nombre varchar_pattern_ops);


--
-- Name: proveedores_proveedor_cuit_f372c799_like; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX proveedores_proveedor_cuit_f372c799_like ON public.proveedores_proveedor USING btree (cuit varchar_pattern_ops);


--
-- Name: proveedores_proveedor_localidad_id_f5e675b0; Type: INDEX; Schema: public; Owner: enredarteadmin
--

CREATE INDEX proveedores_proveedor_localidad_id_f5e675b0 ON public.proveedores_proveedor USING btree (localidad_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: compras_compra compras_compra_proveedor_id_d647dfa3_fk_proveedor; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.compras_compra
    ADD CONSTRAINT compras_compra_proveedor_id_d647dfa3_fk_proveedor FOREIGN KEY (proveedor_id) REFERENCES public.proveedores_proveedor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: compras_insumoscompra compras_insumoscompra_compra_id_1a5038d1_fk_compras_compra_id; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.compras_insumoscompra
    ADD CONSTRAINT compras_insumoscompra_compra_id_1a5038d1_fk_compras_compra_id FOREIGN KEY (compra_id) REFERENCES public.compras_compra(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: compras_insumoscompra compras_insumoscompra_insumo_id_29202c98_fk_productos_insumo_id; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.compras_insumoscompra
    ADD CONSTRAINT compras_insumoscompra_insumo_id_29202c98_fk_productos_insumo_id FOREIGN KEY (insumo_id) REFERENCES public.productos_insumo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: clientes_cliente gestion_cliente_localidad_id_0a7e274d_fk_gestion_localidad_id; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.clientes_cliente
    ADD CONSTRAINT gestion_cliente_localidad_id_0a7e274d_fk_gestion_localidad_id FOREIGN KEY (localidad_id) REFERENCES public.gestion_localidad(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gestion_localidad gestion_localidad_provincia_id_4b057c4d_fk_gestion_provincia_id; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.gestion_localidad
    ADD CONSTRAINT gestion_localidad_provincia_id_4b057c4d_fk_gestion_provincia_id FOREIGN KEY (provincia_id) REFERENCES public.gestion_provincia(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pedidos_pedido pedidos_pedido_cliente_id_84f4fc73_fk_clientes_cliente_id; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.pedidos_pedido
    ADD CONSTRAINT pedidos_pedido_cliente_id_84f4fc73_fk_clientes_cliente_id FOREIGN KEY (cliente_id) REFERENCES public.clientes_cliente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pedidos_productospedido pedidos_productosped_producto_id_24373755_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.pedidos_productospedido
    ADD CONSTRAINT pedidos_productosped_producto_id_24373755_fk_productos FOREIGN KEY (producto_id) REFERENCES public.productos_producto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pedidos_productospedido pedidos_productospedido_pedido_id_281119d2_fk_pedidos_pedido_id; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.pedidos_productospedido
    ADD CONSTRAINT pedidos_productospedido_pedido_id_281119d2_fk_pedidos_pedido_id FOREIGN KEY (pedido_id) REFERENCES public.pedidos_pedido(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_caracteristicasproducto productos_caracteris_caracteristica_id_673102d7_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_caracteristicasproducto
    ADD CONSTRAINT productos_caracteris_caracteristica_id_673102d7_fk_productos FOREIGN KEY (caracteristica_id) REFERENCES public.productos_caracteristica(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_caracteristicasproducto productos_caracteris_producto_id_de124b3b_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_caracteristicasproducto
    ADD CONSTRAINT productos_caracteris_producto_id_de124b3b_fk_productos FOREIGN KEY (producto_id) REFERENCES public.productos_producto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_insumo_proveedores productos_insumo_pro_insumo_id_914827de_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumo_proveedores
    ADD CONSTRAINT productos_insumo_pro_insumo_id_914827de_fk_productos FOREIGN KEY (insumo_id) REFERENCES public.productos_insumo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_insumo_proveedores productos_insumo_pro_proveedor_id_b74124a9_fk_proveedor; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumo_proveedores
    ADD CONSTRAINT productos_insumo_pro_proveedor_id_b74124a9_fk_proveedor FOREIGN KEY (proveedor_id) REFERENCES public.proveedores_proveedor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_insumo productos_insumo_unidad_medida_id_39ad036e_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumo
    ADD CONSTRAINT productos_insumo_unidad_medida_id_39ad036e_fk_productos FOREIGN KEY (unidad_medida_id) REFERENCES public.productos_unidad(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_insumosproducto productos_insumospro_insumo_id_711ec9bd_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumosproducto
    ADD CONSTRAINT productos_insumospro_insumo_id_711ec9bd_fk_productos FOREIGN KEY (insumo_id) REFERENCES public.productos_insumo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_insumosproducto productos_insumospro_producto_id_ce42865b_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_insumosproducto
    ADD CONSTRAINT productos_insumospro_producto_id_ce42865b_fk_productos FOREIGN KEY (producto_id) REFERENCES public.productos_producto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_productimage productos_productima_producto_id_30689d5d_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_productimage
    ADD CONSTRAINT productos_productima_producto_id_30689d5d_fk_productos FOREIGN KEY (producto_id) REFERENCES public.productos_producto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_stockinsumo productos_stockinsumo_insumo_id_cec573dd_fk_productos_insumo_id; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.productos_stockinsumo
    ADD CONSTRAINT productos_stockinsumo_insumo_id_cec573dd_fk_productos_insumo_id FOREIGN KEY (insumo_id) REFERENCES public.productos_insumo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: proveedores_proveedor proveedores_proveedo_localidad_id_f5e675b0_fk_gestion_l; Type: FK CONSTRAINT; Schema: public; Owner: enredarteadmin
--

ALTER TABLE ONLY public.proveedores_proveedor
    ADD CONSTRAINT proveedores_proveedo_localidad_id_f5e675b0_fk_gestion_l FOREIGN KEY (localidad_id) REFERENCES public.gestion_localidad(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

